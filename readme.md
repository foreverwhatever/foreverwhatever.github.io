---
anaconda-cloud: !!python/object:nbformat.notebooknode.NotebookNode {_allownew: true}
config_dir: /Users/tonyfast/.jupyter
kernelspec: !!python/object/new:nbformat.notebooknode.NotebookNode
  dictitems: {display_name: Python 3, language: python, name: python3}
  state: {_allownew: true}
language_info: !!python/object/new:nbformat.notebooknode.NotebookNode
  dictitems:
    codemirror_mode: !!python/object/new:nbformat.notebooknode.NotebookNode
      dictitems: {name: ipython, version: 3}
      state: {_allownew: true}
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.5.3
  state: {_allownew: true}
metadata: !!python/object/apply:nbconvert.exporters.exporter.ResourcesDict
  dictitems: {modified_date: 'June 24, 2017', name: readme, path: ''}
output_extension: .md
output_files_dir: readme_files
unique_key: readme
---

`foreverwhatever.github.io` is Tony Fast's personal journal of computational documents.


```python
%load_ext literacy.template
```
## The __build__ branch

The __build__ branch uses __travis-ci__ to transpile notebooks to a jekyll site on the __master__ 
branch.  When __master__ updates, the standard github pages __jekyll__ build is used.

### A collection of notebooks

Create a collection of ___notebooks__. It folder is the source of __markdown__, __json__, and
__python__ copies of the collection.
### Markdown

The markdown __nbconvert__ configuration is *_layouts/markdown.py*
        !jupyter nbconvert --config _layouts/markdown.py readme.ipynb

* Notebooks beginning with __Numbers__ are inferred as ___posts__



```python
!jupyter nbconvert --config _layouts/markdown.py --output-dir _posts _notebooks/[0-9]*.ipynb
```


* Notebooks beginning with __Letters__ are inferred as ___docs__



```python
!jupyter nbconvert --config _layouts/markdown.py --output-dir _docs _notebooks/[a-z,A-Z]*.ipynb
```

### Python

The python __nbconvert__ configuration is *_layouts/python.py*.  The module is in a _non_-__Jekyll__ namespace;
I personally chose __whatever__.



```python
!jupyter nbconvert --config _layouts/python.py --output-dir=whatever _notebooks/*.ipynb
```
### Data

The data __nbconvert__ configuration is *_layouts/data.py*



```python
!jupyter nbconvert --to notebook --config _layouts/data.py _notebooks/*.ipynb
```
