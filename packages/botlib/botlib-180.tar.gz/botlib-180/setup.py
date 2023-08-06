# This file is placed in the Public Domain.
# pylint: disable=C0116


"botlib's setuptools setup.py"


from setuptools import setup


def read():
    return open("README.rst", "r").read()


setup(
    name="botlib",
    version="180",
    url="https://github.com/bthate/botlib",
    author="Bart Thate",
    author_email="bthate67@gmail.com",
    description="The Python3 bot Namespace",
    long_description=read(),
    long_description_content_type="text/x-rst",
    license="Public Domain",
    packages=["bot"],
    zip_safe=True,
    include_package_data=True,
    data_files=[
                ("share/doc/botlib", ["README.rst",]),
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
)
