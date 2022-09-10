#!/usr/bin/env python

from setuptools import setup, find_packages

requirements = []


setup(
    author="Danila Mikhaltsov",
    author_email="danila-mikh@ya.ru",
    python_requires=">=3.6",
    description="Decide what to watch using the power of randomness!",
    entry_points={
        "console_scripts": [
            "decide=decide_what_to_watch.main:main",
        ],
    },
    packages=find_packages(include=["decide_what_to_watch"]),
    install_requires=requirements,
    license="MIT license",
    name="decide_what_to_watch",
    url="https://github.com/m-danya/decide-what-to-watch",
    version="0.9.9",
    include_package_data=True,
)
