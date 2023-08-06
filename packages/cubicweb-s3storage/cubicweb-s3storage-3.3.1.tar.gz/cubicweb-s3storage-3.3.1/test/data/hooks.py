from cubicweb.server.hook import Hook
from cubicweb_s3storage.storages import S3Storage


class S3StorageStartupHook(Hook):
    __regid__ = "s3tests.server-startup-hook"
    events = ("server_startup", "server_maintenance")

    def __call__(self):
        storage = S3Storage("test-bucket")
        self.repo.system_source.set_storage("Image", "data", storage)
