---
layout: post
modified_date: June 24, 2017
name: 2017-01-01-triangles
path: _notebooks

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


# <del>`fidget`</del> <small>a `pythonic` functional programming `object`</small>

> ...posers juxtapose juxtapositions

> composers compose compositions


```python
from fidget import pipes as a, maps; an = the = then = a
from copy import copy
import pandas, requests, toolz
```


```python
triangles = a.combinations(r=2).zip(list('ABC'))[maps.concat().list()].concatv([list('ABC')]).list()('DEF')
triangles
```


```python
positions = {
    'A': [-1, 0], 'B': [0, 1], 'C': [1, 0],
    'D': [-.5, .5], 'E': [0, 0], 'F': [.5, .5],
}
```
