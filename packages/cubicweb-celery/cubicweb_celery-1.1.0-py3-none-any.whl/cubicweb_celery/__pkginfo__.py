# pylint: disable=W0622
"""cubicweb-celery application packaging information"""


cubename = "celery"
modname = "cubicweb_" + cubename
distname = "cubicweb-" + cubename

numversion = (1, 1, 0)
version = ".".join(str(num) for num in numversion)

license = "LGPL"
author = "Logilab"
author_email = "contact@logilab.fr"
description = "Celery cube"
web = "https://forge.extranet.logilab.fr/cubicweb/cubes/%s" % cubename

__depends__ = {
    "celery": "~=5.0",
    'cubicweb': ">= 3.38.0, < 3.39.0",
}
__recommends__ = {}

classifiers = [
    "Environment :: Web Environment",
    "Framework :: CubicWeb",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: JavaScript",
]
