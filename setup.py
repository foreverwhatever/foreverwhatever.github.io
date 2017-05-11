# coding: utf-8

# In[2]:

from plumbum import local, FG  # noqa: E402
from setuptools import Command, setup, Distribution  # noqa: E402, F401
from setuptools.command.develop import develop
import os

# Base class for no-arg commands

# In[3]:

packages = ['whatever', 'forever']

# In[4]:


class CommandBase(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


# Conversion rules for all of the notebooks
# 
#         from setuptools import  Distribution
#         Convert(Distribution()).run()

# In[20]:


class Convert(CommandBase):
    def run(self):
        convert = local['jupyter']['nbconvert']['--config']['config.py']
        convert['--to']['script']['--template']['_layouts/docify.tpl']['setup.ipynb']['_posts/__init__.ipynb']['_pages/*.ipynb'] & FG
        convert['--to']['markdown']['--template']['_layouts/jekyll.md.tpl']['_posts/*.ipynb']['_pages/*.ipynb'] & FG
        convert['--to']['html']['--template']['_layouts/jekyll.html.tpl']['index.ipynb'] & FG
        local['yapf']['-i']['-r']['_pages'] & FG
        local['echo']["Conversion complete"] & FG
        pass


# In[21]:

from setuptools import Distribution

# Watcher to convert notebooks to python.

# In[ ]:


class Watch(CommandBase):
    def run(self):
        try:
            local['watchmedo']['tricks-from']['tricks.yml'] & FG
        except KeyboardInterrupt:
            pass


# In[ ]:


class Develop(develop):
    def run(self):
        for folder, package in zip(['_posts', '_pages'], packages):
            try:
                os.unlink(package)
            except FileNotFoundError:
                pass
            os.symlink(folder, package)
        develop.run(self)


# In[ ]:

setup(
    name="forever-whatever",
    version="0.0.0",
    #     package_dir={'whatever': '_posts', 'forever': '_pages', },
    packages=packages,
    cmdclass={'watch': Watch,
              'convert': Convert,
              'developer': Develop})

# __*fin*__
