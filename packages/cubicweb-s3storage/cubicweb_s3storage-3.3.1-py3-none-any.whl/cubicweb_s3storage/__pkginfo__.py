# pylint: disable=W0622
"""cubicweb-s3storage application packaging information"""


modname = "cubicweb_s3storage"
distname = "cubicweb-s3storage"

numversion = (3, 3, 1)
version = ".".join(str(num) for num in numversion)

license = "LGPL"
author = "LOGILAB S.A. (Paris, FRANCE)"
author_email = "contact@logilab.fr"
description = "A Cubicweb Storage that stores the data on S3"
web = "https://forge.extranet.logilab.fr/cubicweb/cubes/%s" % distname

__depends__ = {
    "cubicweb": ">= 3.24.7, < 3.39.0",
    "six": ">= 1.4.0",
    "boto3": None,
}
__recommends__ = {}

classifiers = [
    "Environment :: Web Environment",
    "Framework :: CubicWeb",
    "Programming Language :: Python",
    "Programming Language :: JavaScript",
]
