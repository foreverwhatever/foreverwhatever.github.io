# coding: utf-8


# __*fin*__

from setuptools import find_packages, Command, setup, Distribution # noqa: E402, F401s
import os

class CommandBase(Command):
    """Base class for no-arg commands"""
    user_options = []
    def initialize_options(self): pass
    def finalize_options(self): pass

class Readme(CommandBase):
    """Conversion rules for all of the notebooks
    
            from setuptools import  Distribution
            Convert(Distribution()).run()
    
    * Convert notebook to python code on master
    * Format python code
    * Convert to notebook to Markdown post on master
    * Convert index.html
    * Convert setup"""
    def run(self):
        get_ipython().magic('load_ext literacy')
        import readme
        get_ipython().system('echo "Conversion complete"')

# Watcher to convert notebooks to python.

setup(
    name="forever-whatever",
    version="0.0.0",
    packages=find_packages(),
    cmdclass={'readme': Readme}
)
# !jupyter nbconvert --config _layouts/python.py  setup.ipynb# __*fin*__