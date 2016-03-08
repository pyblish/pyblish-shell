from distutils.core import setup

__import__("py2exe")
setup(
    console=["app.py"],
    options={
        "py2exe": {
            "unbuffered": True,
            "excludes": [
                "pyblish",
                "pyblish_qml",
                "pyblish_rpc",
            ],
            "includes": [
                "getpass",
                "contextlib",
                "ConfigParser",
                "xml.etree.ElementTree",
                "xmlrpclib",
                "SimpleXMLRPCServer",
                "json",
                "urllib2",
                "numbers",
            ]
        }
    }
)
