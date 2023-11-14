# -*- coding: utf-8 -*-

import os
import sys
from shutil import rmtree

from setuptools import setup, Command

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


class PublishCommand(Command):
    """Support setup.py publish."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPi via Twine…")
        os.system("twine upload dist/*")

        sys.exit()


setup(
    name="daftlistings",
    version="2.0.4",
    description="A library that enables programmatic interaction with daft.ie. Daft.ie has nationwide coverage and contains about 80% of the total available properties in Ireland.",
    long_description=long_descr,
    long_description_content_type="text/markdown",
    url="https://github.com/AnthonyBloomer/daftlistings",
    author="Anthony Bloomer",
    keywords=["daft", "real estate", "daft.ie"],
    author_email="ant0@protonmail.ch",
    license="MIT",
    packages=["daftlistings"],
    install_requires=["requests", "folium"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
    ],
    cmdclass={
        "publish": PublishCommand,
    },
    zip_safe=False,
)
