# copyright 2018-2022 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This file is part of CubicWeb.
#
# CubicWeb is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# CubicWeb is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with CubicWeb.  If not, see <http://www.gnu.org/licenses/>.

"""custom storages for S3"""

import uuid
from logging import getLogger

import os
import boto3

from cubicweb import Binary, set_log_methods
from cubicweb.server.sources.storages import Storage
from cubicweb.server.edition import EditedEntity
from cubicweb.server.hook import DataOperationMixIn, LateOperation


class S3Storage(Storage):
    is_source_callback = True
    KEY_SEPARATOR = "#"

    def __init__(self, bucket, suffix=".tmp"):
        self.s3cnx = self._s3_client()
        self.bucket = bucket
        self.suffix = suffix

    @classmethod
    def _s3_client(cls):
        endpoint_url = os.environ.get("AWS_S3_ENDPOINT_URL")
        if endpoint_url:
            cls.debug(f"Using custom S3 endpoint url {endpoint_url}")
        return boto3.client("s3", endpoint_url=endpoint_url)

    def callback(self, source, cnx, value):
        """see docstring for prototype, which vary according to is_source_callback"""
        key = source.binary_to_str(value).decode("utf-8")
        if (
            cnx.repo.config["s3-transaction-suffix-key"]
            and cnx.commit_state == "precommit"
        ):
            # download suffixed key if it exists
            # FIXME need a way to check that the attribute is actually edited
            try:
                suffixed_key = self.suffixed_key(key)
                return self.get_s3_object(cnx, suffixed_key)
            except Exception:
                pass
        try:
            return self.get_s3_object(cnx, key)
        except Exception as ex:
            source.critical("can't retrieve S3 object %s: %s", key, ex)
            return None

    def entity_added(self, entity, attr):
        """an entity using this storage for attr has been added"""
        if entity._cw.transaction_data.get("fs_importing"):
            # fs_importing allows to change S3 key saved in database
            entity._cw_dont_cache_attribute(attr, repo_side=True)
            key = entity.cw_edited[attr].getvalue()
            key = key.decode("utf-8")
            try:
                return self.get_s3_object(entity._cw, key)
            except Exception:
                return None

        binary = entity.cw_edited.pop(attr)
        if binary is None:
            # remove S3 key
            entity.cw_edited.edited_attribute(attr, None)
            self.entity_deleted(entity, attr)
        else:
            oldkey = self.get_s3_key(entity, attr)
            if oldkey is not None:
                oldkey, _ = self.parse_key(oldkey)
            key = self.new_s3_key(entity, attr)
            # copy Binary value, workaround for boto3 bug
            # https://github.com/boto/s3transfer/issues/80
            # .read() is required since Binary can't wrap itself
            binary.seek(0)
            buffer = Binary(binary.read())
            binary.seek(0)
            if entity._cw.repo.config["s3-transaction-suffix-key"]:
                upload_key = self.suffixed_key(key)
            else:
                upload_key = key
            extra_args = self.get_upload_extra_args(entity, attr, key)

            put_object_result = self.s3cnx.put_object(
                Body=buffer, Bucket=self.bucket, Key=upload_key, **extra_args
            )
            buffer.close()
            version_id = put_object_result.get("VersionId", None)
            # save S3 key
            entity = self.save_s3_key(entity, attr, upload_key, version_id)

            # when key is suffixed, move to final key in post commit event
            # remove temporary key on rollback
            S3AddFileOp.get_instance(entity._cw).add_data((self, key, entity.eid, attr))
            self.info(
                "Uploaded %s.%s (%s/%s) to S3",
                entity.eid,
                attr,
                self.bucket,
                upload_key,
            )
            if oldkey is not None and oldkey != key:
                # remove unneeded old key
                self.delay_deletion(entity, attr, oldkey)
        return binary

    def get_upload_extra_args(self, _entity, _attr, _key):
        """Additional options for boto3's upload_fileobj method.
        Documentation for supported options can be found at:
        https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html#the-extraargs-parameter
        """
        return {}

    def entity_updated(self, entity, attr):
        """an entity using this storage for attr has been updated"""
        return self.entity_added(entity, attr)

    def entity_deleted(self, entity, attr):
        """an entity using this storage for attr has been deleted"""
        key = self.get_s3_key(entity, attr)
        if key is None:
            # no key to remove
            return
        key, _ = self.parse_key(key)
        self.delay_deletion(entity, attr, key)

    def delay_deletion(self, entity, attr, key):
        if entity._cw.repo.config["s3-auto-delete"]:
            # delete key in a post commit event
            S3DeleteFileOp.get_instance(entity._cw).add_data(
                (self, key, entity.eid, attr)
            )
            self.info(
                "Delaying deletion for %s.%s (%s/%s) in S3",
                entity.eid,
                attr,
                self.bucket,
                key,
            )

    def migrate_entity(self, entity, attribute):
        """migrate an entity attribute to the storage"""
        entity.cw_edited = EditedEntity(entity, **entity.cw_attr_cache)
        binary = self.entity_added(entity, attribute)
        if binary is not None:
            cnx = entity._cw
            source = cnx.repo.system_source
            attrs = source.preprocess_entity(entity)
            sql = source.sqlgen.update("cw_" + entity.cw_etype, attrs, ["cw_eid"])
            source.doexec(cnx, sql, attrs)
        entity.cw_edited = None

    def save_s3_key(self, entity, attr, key, version_id=None):
        """
        Save the s3 key into the entity bytes attribute
        """
        id_string = key
        if (
            entity._cw.repo.config["s3-activate-object-versioning"]
            and version_id is not None
        ):
            id_string = self.format_version_id_suffix(key, version_id)
        entity.cw_edited.edited_attribute(attr, Binary(id_string.encode("utf-8")))
        return entity

    def parse_key(self, key):
        try:
            key, version = key.rsplit(self.KEY_SEPARATOR, 1)
        except ValueError:
            return key, None
        return key, version

    def format_version_id_suffix(self, key, version_id):
        """
        Format the string that will store key and version id
        """
        return f"{key}{self.KEY_SEPARATOR}{version_id}"

    def get_s3_key(self, entity, attr):
        """
        Return the S3 key of the S3 object storing the content of attribute
        attr of the entity.
        """
        try:
            rset = entity._cw.execute(
                "Any stkey(D) WHERE X eid {}, X {} D".format(entity.eid, attr)
            )
        except NotImplementedError:
            # may occur when called from migrate_entity, ie. when the storage
            # has not yet been installed
            rset = None
        if rset and rset.rows[0][0]:
            key = rset.rows[0][0].getvalue()
            key = key.decode("utf-8")
            return key
        return None

    def new_s3_key(self, entity, attr):
        """Generate a new key for given entity attr.

        This implementation just returns a random UUID"""
        return str(uuid.uuid1())

    def suffixed_key(self, key):
        return key + self.suffix

    def get_s3_object(self, cnx, key):
        """
        :param cnx: (Object)
        :param key: (string)
        get s3 stored attribute for key
        handle the case of versioned object
        """
        versioning_activated = cnx.repo.config["s3-activate-object-versioning"]
        # check  first : does the key contain a '<separator>'
        key, version_id = self.parse_key(key)

        # if object-versioning is activated use the version_id
        if versioning_activated and version_id is not None:
            return self.download(key, VersionId=version_id)
        return self.download(key)

    def download(self, key, **kwargs):
        """
        :param key: (string)
        :param kwargs: (dict) Keys must be compatible with method S3.Client.put_object
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_object
        """
        result = self.s3cnx.get_object(Bucket=self.bucket, Key=key, **kwargs)
        self.info("Downloaded %s/%s from S3", self.bucket, key)
        return Binary(result["Body"].read())


class S3AddFileOp(DataOperationMixIn, LateOperation):
    containercls = list

    def postcommit_event(self):
        if not self.cnx.repo.config["s3-transaction-suffix-key"]:
            return
        consumed_keys = set()
        for storage, key, eid, attr in self.get_data():
            if key in consumed_keys:
                continue
            consumed_keys.add(key)
            suffixed_key = storage.suffixed_key(key)
            storage.s3cnx.copy_object(
                Bucket=storage.bucket,
                CopySource={"Bucket": storage.bucket, "Key": suffixed_key},
                Key=key,
            )
            storage.s3cnx.delete_object(Bucket=storage.bucket, Key=suffixed_key)
            self.info(
                "Moved temporary object for %s.%s (%s/%s to %s/%s)" " in S3",
                eid,
                attr,
                storage.bucket,
                suffixed_key,
                storage.bucket,
                key,
            )

    def rollback_event(self):
        for storage, key, eid, attr in self.get_data():
            if self.cnx.repo.config["s3-transaction-suffix-key"]:
                upload_key = storage.suffixed_key(key)
            else:
                upload_key = key
            storage.s3cnx.delete_object(Bucket=storage.bucket, Key=upload_key)
            self.info(
                "Deleted temporary object for %s.%s (%s/%s) in S3",
                eid,
                attr,
                storage.bucket,
                upload_key,
            )


class S3DeleteFileOp(DataOperationMixIn, LateOperation):
    containercls = list

    def postcommit_event(self):
        for storage, key, eid, attr in self.get_data():
            self.info(
                "Deleting object %s.%s (%s/%s) from S3", eid, attr, storage.bucket, key
            )
            resp = storage.s3cnx.delete_object(Bucket=storage.bucket, Key=key)
            if resp.get("ResponseMetadata", {}).get("HTTPStatusCode") >= 300:
                self.error("S3 object deletion FAILED: %s", resp)
            else:
                self.debug("S3 object deletion OK: %s", resp)


set_log_methods(S3Storage, getLogger("cube.s3storage.storages.s3storage"))
