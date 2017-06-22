# coding: utf-8

from plumbum import local, FG  # noqa: E402
from setuptools import find_packages, Command, setup, Distribution  # noqa: E402, F401s
import os


class CommandBase(Command):
    """Base class for no-arg commands
    """
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class Convert(CommandBase):
    """Conversion rules for all of the notebooks
    
            from setuptools import  Distribution
            Convert(Distribution()).run()
    """

    def run(self):
        convert = local['jupyter']['nbconvert']['--config']['config.py']
        convert['--to']['script']['--template']['_layouts/docify.tpl']['setup.ipynb']['_posts/__init__.ipynb']['_pages/*.ipynb'] & FG
        convert['--to']['markdown']['--template']['_layouts/jekyll.md.tpl']['_posts/*.ipynb']['_pages/*.ipynb'] & FG
        convert['--to']['html']['--template']['_layouts/jekyll.html.tpl']['index.ipynb'] & FG
        local['yapf']['-i']['-r']['_pages'] & FG
        local['echo']["Conversion complete"] & FG
        pass


from setuptools import Distribution


class Watch(CommandBase):
    """Watcher to convert notebooks to python.
    """

    def run(self):
        try:
            local['watchmedo']['tricks-from']['tricks.yml'] & FG
        except KeyboardInterrupt:
            pass


# !jupyter nbconvert --to python --config _layouts/config.py --template _layouts/docify.tpl setup.ipynb

setup(
    name="forever-whatever",
    version="0.0.0",
    packages=find_packages(),
    cmdclass={'watch': Watch,
              'convert': Convert})
# __*fin*__# 
