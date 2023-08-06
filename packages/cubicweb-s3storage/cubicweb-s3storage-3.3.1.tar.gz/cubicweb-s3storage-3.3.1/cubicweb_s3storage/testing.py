import boto3
from unittest.mock import patch
from moto import mock_s3


class S3StorageTestMixin:

    s3_bucket = "test-bucket"

    def setUp(self):
        s3_mock = mock_s3()
        s3_mock.start()
        resource = boto3.resource("s3", region_name="us-east-1")
        self.s3_bucket = resource.create_bucket(Bucket=self.s3_bucket)
        patched_storage_s3_client = patch(
            "cubicweb_s3storage.storages.S3Storage._s3_client",
            return_value=boto3.client("s3"),
        )
        patched_storage_s3_client.start()
        self._mocks = [
            s3_mock,
            patched_storage_s3_client,
        ]
        super().setUp()

    def tearDown(self):
        super().tearDown()
        while self._mocks:
            self._mocks.pop().stop()
