Summary
-------

A Cubicweb Storage that stores the data on S3.

It is a standard Cubicweb_ Storage, similar to the BytesFileSystemStorage_. For
example, if you want to store File.data payloads in S3, you should create an
S3Storage instance, typically in a startup hook, as::


  from cubicweb.server.hook import Hook
  from cubicweb_s3storage.storages import S3Storage

  class S3StorageStartupHook(Hook):
      __regid__ = 'mycube.server-startup-hook'
      events = ('server_startup', 'server_maintenance')

      def __call__(self):
          storage = S3Storage('s3_bucket')
          self.repo.system_source.set_storage('File', 'data', storage)

By default, S3 object keys (ie. S3 object identifiers) are random UUID
generated at entity creation time. If you want to implement another key
generation algorithm, you must write overload ``S3Storage.new_s3_key()``
method.


Communications with AWS are handled by boto3_.


.. Warning:: 

   There is no cache, for now, so every time you read an entity
   attribute that is stored on S3, it will be downloaded from bucket provider.

Configuration
-------------

The S3Storage class constructor needs an S3 bucket name.

If you want to put your aws credentials in an other file than the default
(``~/.aws/credentials``), you must set the ``AWS_CONFIG_FILE`` environment
variable.

If you want to use another profile name than ``default``, set the
``AWS_PROFILE`` environment variable.

If you prefer to configure AWS credentials by environment variables
(eg. when using docker), you can use the following variables:

- AWS_ACCESS_KEY_ID: the access key for your AWS account,

- AWS_SECRET_ACCESS_KEY: the secret key for your AWS account.

Please read `boto3 documentation`_ for more details.

Further configuration
---------------------

In some cases you might want to use compatible S3 storage which is not on
AWS.

For this you have the following variables :

- AWS_S3_ENDPOINT_URL: endpoint url for your alternative S3 storage

This enables the use of a `minio server <https://min.io>`_, see
`their documentation about endpoints
<https://docs.min.io/docs/aws-cli-with-minio>`_.

Note : this type of variable `has been requested upstream
<https://github.com/boto/boto3/issues/2099>`_
(and related `aws-cli <https://github.com/aws/aws-cli/issues/4454>`_).


.. _`boto3 documentation`: https://boto3.readthedocs.io/en/stable/guide/configuration.html#shared-credentials-file
.. _boto3: https://github.com/boto/boto3
.. _Cubicweb: https://www.cubicweb.org/project/cubicweb
.. _BytesFileSystemStorage: http://cubicweb.readthedocs.io/en/3.26.2/tutorials/advanced/part03_bfss

