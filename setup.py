# coding: utf-8

# __*fin*__

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
    
    * Convert notebook to python code on master
    * Format python code
    * Convert to notebook to Markdown post on master
    * Convert index.html
    * Convert setup
    """

    def run(self):
        get_ipython().system(
            'jupyter nbconvert --to python --template _layouts/docify.tpl --config _layouts/config.py --output-dir whatever _data/*.ipynb'
        )
        get_ipython().system(
            'jupyter nbconvert --to markdown --template _layouts/jekyll.md.tpl --config _layouts/mdconfig.py --output-dir _posts _data/*.ipynb'
        )
        get_ipython().system('yapf -i -r .')
        get_ipython().system('echo "Conversion complete"')


# 
class Watch(CommandBase):
    """Watcher to convert notebooks to python.
    """

    def run(self):
        try:
            get_ipython().system('watchmedo tricks-from tricks.yml')
        except KeyboardInterrupt:
            pass


setup(
    name="forever-whatever",
    version="0.0.0",
    packages=find_packages(),
    cmdclass={'watch': Watch,
              'convert': Convert})
# !jupyter nbconvert --to python --template _layouts/docify.tpl --config _layouts/config.py setup.ipynb# __*fin*__
