#!/usr/bin/env python

from distutils.core import setup

VERSION = "0.1.2"

setup(
    name="kazy",
    packages=["kazy"],
    description="Highlights STDIN data",

    license='MIT',

    author="Yauhen Shulitski",
    author_email="jsnjack@gmail.com",

    url="https://github.com/jsnjack/kazy",

    scripts=["bin/kazy"],

    keywords=["logging", "highlight", "stdin"],

    version=VERSION,
    download_url="https://github.com/jsnjack/kazy/tarball/{}".format(VERSION)
)
