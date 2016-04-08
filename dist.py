"""Create distributions of pyblish-shell

Platforms:
- zip
- windows (requires InnoSetup)

Example:
    $ python dist.py windows --clean
    $ python dist.py zip

"""

import os
import sys
import shutil
import zipfile
import argparse
import subprocess

from pyblish_shell import version
build = (os.environ.get("APPVEYOR_BUILD_NUMBER") or
         os.environ.get("TRAVIS_BUILD_NUMBER") or
         0)


def build_inno_exe(src, dst):
    """Create Windows installer using Inno Setup

    Arguments:
        src (str): Path to bundle, e.g. build
        dst (str): Output directory in which to compile installer, e.g. dist

    """

    print("Creating installer..")
    try:
        iscc = subprocess.check_output(["where", "iscc"]).strip()
    except subprocess.CalledProcessError:
        sys.stderr.write("Could not find Inno Setup\n")
        exit(1)

    setup = os.path.join(os.getcwd(), "setup.iss")

    print("Compiling \"%s\" using \"%s\"" % (setup, iscc))
    subprocess.call([iscc,
                     "/dMyVersion=%s-build%s" % (version, build),
                     "/dMyOutputDir=%s" % dst,
                     setup])

    print("Successfully created installer")


def build_zip(src, dst, platform):
    """Create zip archive

    Arguments:
        src (str): Path to bundle, e.g. build
        dst (str): Output directory in which to compile installer, e.g. dist

    """

    dst = os.path.join(
        dst, "pyblish-shell-{version}-build{build}-{platform}-x64.zip".format(
            version=version,
            build=build,
            platform=platform)
    )

    print("Creating archive %s" % dst)

    with zipfile.ZipFile(dst, "w") as zf:
        for base, dirs, fnames in os.walk(src):
            for fname in fnames:
                abspath = os.path.join(base, fname)
                print("Adding %s" % abspath)
                zf.write(abspath,
                         os.path.relpath(abspath, src),
                         compress_type=zipfile.ZIP_DEFLATED)

    print("%s created" % dst)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("platform")
    parser.add_argument("--clean", action="store_true")

    args = parser.parse_args()

    src = os.path.abspath("build")
    dst = os.path.abspath("dist")

    if args.clean and os.path.exists(dst):
        print("Cleaning dist directory..")

        try:
            shutil.rmtree(dst)
        except:
            sys.stderr.write("Could not remove dist directory")
            exit(1)

    try:
        os.makedirs(dst)
    except:
        pass  # Already exists

    if args.platform == "windows":
        build_zip(src, dst, "win32")
        build_inno_exe(src, dst)
    
    elif args.platform == "osx":
        build_zip(src, dst, "osx")

    else:
        sys.stderr.write("platform '%s' not supported.\n")
