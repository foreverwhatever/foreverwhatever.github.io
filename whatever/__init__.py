
# coding: utf-8

# In[ ]:

from forever.ipynb import notebook_module
import os, glob, sys
directory, ext = os.path.dirname(__file__), 'ipynb'
for file in glob.glob(os.path.sep.join([directory, os.path.extsep.join(['*', ext])])):
    name = file.lstrip(directory).rstrip(ext).rstrip('.')
    if all(map(str.isnumeric, name[:4])):
        locals()[name] = notebook_module(name, file)

