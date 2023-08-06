import re
from contextlib import contextmanager
from unittest.mock import patch

from cubicweb.server.sources import storages
from cubicweb.devtools.testlib import CubicWebTC
from cubicweb import Binary
from cubicweb.server.migractions import ServerMigrationHelper
from cubicweb_s3storage import testing


def create_image(cnx, data=b"the-data", **kwargs):
    return cnx.create_entity("Image", data=Binary(data), **kwargs)


class S3StorageVersionedTC(testing.S3StorageTestMixin, CubicWebTC):
    def test_s3key_gen(self):
        self.s3_bucket.Versioning().enable()
        self.repo.vreg.config["s3-activate-object-versioning"] = True
        s3storage = self.repo.system_source.storage("Image", "data")
        with self.admin_access.client_cnx() as cnx:
            fobj = create_image(cnx, b"some content")
            cnx.commit()
            eid = fobj.eid
            k1 = s3storage.get_s3_key(fobj, "data")
        with self.admin_access.client_cnx() as cnx:
            fobj = cnx.find("Image", eid=eid).one()
            k2 = s3storage.get_s3_key(fobj, "data")
        self.assertEqual(k1, k2)

    def test_entity_create_versioning(self):
        self.s3_bucket.Versioning().enable()
        self.repo.vreg.config["s3-activate-object-versioning"] = True
        with self.admin_access.client_cnx() as cnx:
            eid = create_image(cnx, b"some content").eid
            cnx.commit()

            key = cnx.execute(
                "Any STKEY(D) WHERE X is Image, X data D, " "X eid %(eid)s",
                {"eid": eid},
            ).rows[0][0]

            key = key.getvalue().decode()

            s3storage = self.repo.system_source.storage("Image", "data")
            key, _ = s3storage.parse_key(key)
        data = self.s3_bucket.Object(key).get()["Body"].read()
        self.assertEqual(data, b"some content")

    def test_entity_create_with_same_key(self):
        self.s3_bucket.Versioning().enable()
        self.repo.vreg.config["s3-activate-object-versioning"] = True
        s3storage = self.repo.system_source.storage("Image", "data")
        with self.admin_access.client_cnx() as cnx, patch(
            "cubicweb_s3storage.storages.S3Storage.new_s3_key",
            return_value="shared-key",
        ):
            eid = create_image(cnx, b"some content").eid
            _ = create_image(cnx, b"some content").eid
            cnx.commit()
            key = cnx.execute(
                "Any STKEY(D) WHERE X is Image, X data D, " "X eid %(eid)s",
                {"eid": eid},
            ).rows[0][0]
            key = key.getvalue().decode()
            key, _ = s3storage.parse_key(key)
        data = self.s3_bucket.Object(key).get()["Body"].read()
        self.assertEqual(data, b"some content")

    def test_entity_modify(self):
        self.s3_bucket.Versioning().enable()
        self.repo.vreg.config["s3-activate-object-versioning"] = True
        s3storage = self.repo.system_source.storage("Image", "data")
        with self.admin_access.client_cnx() as cnx:
            eid = create_image(cnx, b"some content").eid
            cnx.commit()
        with self.admin_access.client_cnx() as cnx:
            fobj = cnx.find("Image", eid=eid).one()
            fobj.cw_set(data=Binary(b"something else"))
            cnx.commit()
            # retrieve key now as it will have changed by the modification
            key = cnx.execute(
                "Any STKEY(D) WHERE X is Image, X data D, " "X eid %(eid)s",
                {"eid": eid},
            ).rows[0][0]
            key = key.getvalue().decode()
            key, _ = s3storage.parse_key(key)

        data = self.s3_bucket.Object(key).get()["Body"].read()
        self.assertEqual(data, b"something else")

    def test_entity_retrieve(self):
        self.s3_bucket.Versioning().enable()
        self.repo.vreg.config["s3-activate-object-versioning"] = True
        binstuff = "".join(chr(x) for x in range(256))
        binstuff = binstuff.encode()
        with self.admin_access.client_cnx() as cnx:
            eid = create_image(cnx, binstuff).eid
            cnx.commit()

        with self.admin_access.client_cnx() as cnx:
            rset = cnx.execute("Any D WHERE F eid %(eid)s, F data D", {"eid": eid})
            self.assertTrue(rset)
            data = rset.rows[0][0]
        self.assertEqual(data.read(), binstuff)

    def test_entity_delete(self):
        self.s3_bucket.Versioning().enable()
        self.repo.vreg.config["s3-activate-object-versioning"] = True
        s3storage = self.repo.system_source.storage("Image", "data")
        self.repo.vreg.config["s3-auto-delete"] = True
        with self.admin_access.client_cnx() as cnx:
            eid = create_image(cnx, b"some content").eid
            cnx.commit()

            key = cnx.execute(
                "Any STKEY(D) WHERE X is Image, X data D, " "X eid %(eid)s",
                {"eid": eid},
            ).rows[0][0]
            key = key.getvalue().decode()
            key, _ = s3storage.parse_key(key)
        keys = [x.key for x in self.s3_bucket.objects.all()]
        self.assertIn(key, keys)
        with self.admin_access.client_cnx() as cnx:
            cnx.execute("DELETE Image X WHERE X eid %(eid)s", {"eid": eid})
            cnx.commit()
        keys = [x.key for x in self.s3_bucket.objects.all()]
        self.assertNotIn(key, keys)

    def test_upload_content_type(self):
        self.s3_bucket.Versioning().enable()
        self.repo.vreg.config["s3-activate-object-versioning"] = True
        s3storage = self.repo.system_source.storage("Image", "data")
        mime_type = "x-custom/mime-type"
        with self.admin_access.client_cnx() as cnx, patch(
            "cubicweb_s3storage.storages.S3Storage" ".get_upload_extra_args",
            return_value={"ContentType": mime_type},
        ):
            image = create_image(cnx, b"some content")
            cnx.commit()
            s3storage = self.repo.system_source.storage("Image", "data")
            s3_key = s3storage.get_s3_key(image, "data")
            s3_key, _ = s3storage.parse_key(s3_key)
            head = s3storage.s3cnx.head_object(Bucket=self.s3_bucket.name, Key=s3_key)
            self.assertEqual(head["ContentType"], mime_type)


class S3StorageTC(testing.S3StorageTestMixin, CubicWebTC):
    def test_s3key_gen(self):
        s3storage = self.repo.system_source.storage("Image", "data")
        with self.admin_access.client_cnx() as cnx:
            fobj = create_image(cnx, b"some content")
            cnx.commit()
            eid = fobj.eid
            k1 = s3storage.get_s3_key(fobj, "data")
        with self.admin_access.client_cnx() as cnx:
            fobj = cnx.find("Image", eid=eid).one()
            k2 = s3storage.get_s3_key(fobj, "data")
        self.assertEqual(k1, k2)

    def test_entity_create(self):
        with self.admin_access.client_cnx() as cnx:
            eid = create_image(cnx, b"some content").eid
            cnx.commit()

            key = cnx.execute(
                "Any STKEY(D) WHERE X is Image, X data D, " "X eid %(eid)s",
                {"eid": eid},
            ).rows[0][0]
            key = key.getvalue().decode()

        data = self.s3_bucket.Object(key).get()["Body"].read()
        self.assertEqual(data, b"some content")

    def test_entity_create_with_same_key(self):
        with self.admin_access.client_cnx() as cnx, patch(
            "cubicweb_s3storage.storages.S3Storage.new_s3_key",
            return_value="shared-key",
        ):
            eid = create_image(cnx, b"some content").eid
            _ = create_image(cnx, b"some content").eid
            cnx.commit()
            key = cnx.execute(
                "Any STKEY(D) WHERE X is Image, X data D, " "X eid %(eid)s",
                {"eid": eid},
            ).rows[0][0]
            key = key.getvalue().decode()
        data = self.s3_bucket.Object(key).get()["Body"].read()
        self.assertEqual(data, b"some content")

    def test_entity_modify(self):
        with self.admin_access.client_cnx() as cnx:
            eid = create_image(cnx, b"some content").eid
            cnx.commit()
        with self.admin_access.client_cnx() as cnx:
            fobj = cnx.find("Image", eid=eid).one()
            fobj.cw_set(data=Binary(b"something else"))
            cnx.commit()
            # retrieve key now as it will have changed by the modification
            key = cnx.execute(
                "Any STKEY(D) WHERE X is Image, X data D, " "X eid %(eid)s",
                {"eid": eid},
            ).rows[0][0]
            key = key.getvalue().decode()

        data = self.s3_bucket.Object(key).get()["Body"].read()
        self.assertEqual(data, b"something else")

    def test_entity_retrieve(self):
        binstuff = "".join(chr(x) for x in range(256))
        binstuff = binstuff.encode()
        with self.admin_access.client_cnx() as cnx:
            eid = create_image(cnx, binstuff).eid
            cnx.commit()

        with self.admin_access.client_cnx() as cnx:
            rset = cnx.execute("Any D WHERE F eid %(eid)s, F data D", {"eid": eid})
            self.assertTrue(rset)
            data = rset.rows[0][0]
        self.assertEqual(data.read(), binstuff)

    def test_entity_delete(self):
        self.repo.vreg.config["s3-auto-delete"] = True
        with self.admin_access.client_cnx() as cnx:
            eid = create_image(cnx, b"some content").eid
            cnx.commit()

            key = cnx.execute(
                "Any STKEY(D) WHERE X is Image, X data D, " "X eid %(eid)s",
                {"eid": eid},
            ).rows[0][0]
            key = key.getvalue().decode()
        keys = [x.key for x in self.s3_bucket.objects.all()]
        self.assertIn(key, keys)
        with self.admin_access.client_cnx() as cnx:
            cnx.execute("DELETE Image X WHERE X eid %(eid)s", {"eid": eid})
            cnx.commit()
        keys = [x.key for x in self.s3_bucket.objects.all()]
        self.assertNotIn(key, keys)

    def test_upload_content_type(self):
        mime_type = "x-custom/mime-type"
        with self.admin_access.client_cnx() as cnx, patch(
            "cubicweb_s3storage.storages.S3Storage" ".get_upload_extra_args",
            return_value={"ContentType": mime_type},
        ):
            image = create_image(cnx, b"some content")
            cnx.commit()
            s3storage = self.repo.system_source.storage("Image", "data")
            s3_key = s3storage.get_s3_key(image, "data")
            head = s3storage.s3cnx.head_object(Bucket=self.s3_bucket.name, Key=s3_key)
            self.assertEqual(head["ContentType"], mime_type)


class S3StorageMigrationTC(testing.S3StorageTestMixin, CubicWebTC):
    @contextmanager
    def mh(self):
        with self.admin_access.repo_cnx() as cnx:
            yield cnx, ServerMigrationHelper(
                self.repo.config,
                self.repo.schema,
                repo=self.repo,
                cnx=cnx,
                interactive=False,
            )

    def test_entity_migration(self):
        with self.admin_access.client_cnx() as cnx:
            create_image(cnx, thumbnail=Binary(b"some content"))
            cnx.commit()

        # Re-use storage instance of "data" attribute as it already has s3
        # mock activated.
        s3_storage = self.repo.system_source.storage("Image", "data")
        with self.mh() as (cnx, mh):
            storages.set_attribute_storage(self.repo, "Image", "thumbnail", s3_storage)

            mh.cmd_storage_changed("Image", "thumbnail")
            cnx.commit()

        with self.admin_access.client_cnx() as cnx:
            key = cnx.execute("Any STKEY(D) WHERE X is Image, " "X thumbnail D").rows[
                0
            ][0]
            key = key.getvalue().decode()
            # check it looks like an UUID generated by uuid.uuid1()
            # sorry, I'm lazy, this regex is a bit too permissive...
            self.assertTrue(re.match(r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}", key))

            value = cnx.execute("Any D WHERE X is Image, " "X thumbnail D").rows[0][0]
            self.assertEqual(b"some content", value.getvalue())


if __name__ == "__main__":
    from unittest import main

    main()
