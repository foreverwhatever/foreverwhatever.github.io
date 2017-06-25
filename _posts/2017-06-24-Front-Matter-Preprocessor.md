---
config_dir: /home/travis/.jupyter
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
metadata:
  modified_date: June 25, 2017
  name: 2017-06-24-Front-Matter-Preprocessor
  path: _notebooks
output_extension: .md
output_files_dir: 2017-06-24-Front-Matter-Preprocessor_files
unique_key: 2017-06-24-Front-Matter-Preprocessor

---

# Front Matter `nbconvert` preprocessor

Append *metadata* and *resources* as front matter to a notebook; insert a markdown cell at the beginning of notebook.


```python
o = __name__ == '__main__'
if o:
    %reload_ext literacy.template
```
Make sure all Mapping objects are pure python __dict__s



```python
def safe(object):
    if hasattr(object, 'items'):
        object = dict(object)
        for key, value in object.items():
            object.update({key: safe(value)})
    return object
```


```python
class FrontMatter(__import__('nbconvert').preprocessors.Preprocessor):
    def preprocess(self, nb, resources={}):
        source = __import__('yaml').safe_dump(
            safe({**resources, **nb['metadata']}), default_flow_style=False)
        nb['cells'].insert(
            0, __import__('nbformat').v4.new_markdown_cell("""---\n{}\n---\n""".format(source))
        )
        return nb, resources
```


```python
exporter = __import__('nbconvert').get_exporter('markdown')(
    config={'TemplateExporter': {'preprocessors': ['literacy.preprocessors.Dedent', FrontMatter]}})
```
---

> The snippet below shows the composed code.

<pre><code>{{o and exporter.from_filename('2017-06-24-Front-Matter-Preprocessor.ipynb')[0].lstrip()}}</code></pre>
__normalize__ all the values of a collection to a basic `dict` type for `yaml.safe_load` to consume.
