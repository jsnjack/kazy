#!/usr/bin/env python

from distutils.core import setup

setup(
    name="kazy",
    version="0.1",
    description="Highlights STDIN data",

    license='MIT',

    author="Yauhen Shulitski",
    author_email="jsnjack@gmail.com",

    url="https://github.com/jsnjack/kazy",

    packages=["kazy"],

    package_data={
        "kazy": [
            "application/kazy",
        ],
    },

    scripts=["kazy/application/kazy"]
)