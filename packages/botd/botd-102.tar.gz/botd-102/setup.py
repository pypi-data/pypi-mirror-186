# This file is placed in the Public Domain.


from setuptools import setup


def read():
    return open("README.rst", "r").read()


setup(
    name="botd",
    version="102",
    url="https://github.com/bthate/botd",
    author="Bart Thate",
    author_email="bthate67@gmail.com",
    description="24/7 channel daemon",
    long_description=read(),
    long_description_content_type="text/x-rst",
    license="Public Domain",
    zip_safe=True,
    include_package_data=True,
    install_requires=["botlib"],
    packages=["botd"],
    scripts=["bin/botcmd", "bin/botctl", "bin/botd"],
    data_files=[
                ("botd", ["files/botd.service",]),
                ("share/doc/botd", ["README.rst",]),
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
)
