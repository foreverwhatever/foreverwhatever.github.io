
# coding: utf-8

# In[85]:

from os.path import join, dirname
import setuptools


def read(fname):
    with open(join(dirname(__file__), fname)) as f:
        return f.read()

from distutils.core import setup, Command

setuptools.setup(
    name="whatever-forever",
    version="0.0.1",
    author="Tony Fast",
    author_email="tony.fast@bastille.io",
    description="Data sources for my research",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Topic :: Utilities",
        "Framework :: IPython",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Testing",
    ],
    install_requires=[],
    tests_require=[],
)
