from rql.utils import register_function
from logilab.database import FunctionDescr

from cubicweb import Binary

options = (
    (
        "s3-auto-delete",
        {
            "type": "yn",
            "default": True,
            "help": "Delete S3 objects on entity deletion",
            "group": "s3",
            "level": 2,
        },
    ),
    (
        "s3-transaction-suffix-key",
        {
            "type": "yn",
            "default": False,
            "help": "Add a temporary suffix to S3 keys during transaction",
            "group": "s3",
            "level": 2,
        },
    ),
    (
        "s3-activate-object-versioning",
        {
            "type": "yn",
            "default": False,
            "help": "store the objects version-id in database",
            "group": "s3",
            "level": 2,
        },
    ),
)


class STKEY(FunctionDescr):
    """return the S3 key of the bytes attribute stored using the S3 Storage (s3s)"""

    rtype = "Bytes"

    def update_cb_stack(self, stack):
        assert len(stack) == 1
        stack[0] = self.source_execute

    def as_sql(self, backend, args):
        raise NotImplementedError(
            "This callback is only available for S3Storage "
            "managed attribute. Is STKEY() argument S3S managed?"
        )

    def source_execute(self, source, session, value):
        s3key = source.binary_to_str(value)
        try:
            return Binary(s3key)
        except OSError as ex:
            source.critical("can't read %s: %s", s3key, ex)
            return None


register_function(STKEY)
