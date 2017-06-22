---
layout: post
modified_date: May 29, 2017
name: __init__
path: whatever

kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  codemirror_mode:
    name: ipython
    version: 3
  file_extension: .py
  mimetype: text/x-python
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
  version: 3.5.3

---



```python
from forever.ipynb import notebook_module
import os, glob, sys
directory, ext = os.path.dirname(__file__), 'ipynb'
for file in glob.glob(os.path.sep.join([directory, os.path.extsep.join(['*', ext])])):
    name = file.lstrip(directory).rstrip(ext).rstrip('.')
    if all(map(str.isnumeric, name[:4])):
        locals()[name] = notebook_module(name, file)
```
