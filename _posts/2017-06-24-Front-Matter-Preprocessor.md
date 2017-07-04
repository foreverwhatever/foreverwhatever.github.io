---
config_dir: /home/travis/.jupyter
description: Notebook metadata as front matter.
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
layout: post
metadata:
  modified_date: July 4, 2017
  name: 2017-06-24-Front-Matter-Preprocessor
  path: whatever
output_extension: .md
output_files_dir: 2017-06-24-Front-Matter-Preprocessor_files
unique_key: 2017-06-24-Front-Matter-Preprocessor

---

# Front Matter `nbconvert` preprocessor

Append *metadata* and *resources* as front matter to a notebook; insert a markdown cell at the beginning of notebook.



<div class="output_markdown rendered_html output_subarea ">
<p><code>safe</code> will make sure all Mapping objects are pure python <strong>dict</strong></p>

<pre><code>def safe(object):
    if hasattr(object, 'items'):
        object = dict(object)
        for key, value in object.items():
            object.update({key: safe(value)})
    return object</code></pre>

</div>


<div class="output_markdown rendered_html output_subarea ">
<p><code>FrontMatter</code> appends the notebook metadata as a markdown cell at the beginning of the ntoebook.</p>

<pre><code>class FrontMatter(__import__('nbconvert').preprocessors.Preprocessor):
    def preprocess(self, nb, resources={}):
        source = __import__('yaml').safe_dump(
            safe({**resources, **nb['metadata']}), default_flow_style=False)
        nb['cells'].insert(
            0, __import__('nbformat').v4.new_markdown_cell("""---\n{}\n---\n""".format(source))
        )
        return nb, resources</code></pre>

</div>


<div class="output_markdown rendered_html output_subarea ">

<pre><code>    exporter = __import__('nbconvert').get_exporter('markdown')(
        config={'TemplateExporter': {'preprocessors': [FrontMatter]}})</code></pre>

</div>


<div class="output_markdown rendered_html output_subarea ">
<hr>
<blockquote><p>The snippet below shows the composed code.</p>
</blockquote>
<pre><code>---
description: Notebook metadata as front matter.
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
layout: post
metadata:
  modified_date: July 4, 2017
  name: 2017-06-24-Front-Matter-Preprocessor
  path: ''
output_extension: .md
outputs: {}

---


# Front Matter `nbconvert` preprocessor

Append *metadata* and *resources* as front matter to a notebook; insert a markdown cell at the beginning of notebook.


```python
    o = __name__ == '__main__'
    if o:
        %reload_ext literacy
```


```python
<code>safe</code> will make sure all Mapping objects are pure python __dict__

    def safe(object):
        if hasattr(object, 'items'):
            object = dict(object)
            for key, value in object.items():
                object.update({key: safe(value)})
        return object
```


<code>safe</code> will make sure all Mapping objects are pure python __dict__

    def safe(object):
        if hasattr(object, 'items'):
            object = dict(object)
            for key, value in object.items():
                object.update({key: safe(value)})
        return object



```python
<code>FrontMatter</code> appends the notebook metadata as a markdown cell at the beginning of the ntoebook.

    class FrontMatter(__import__('nbconvert').preprocessors.Preprocessor):
        def preprocess(self, nb, resources={}):
            source = __import__('yaml').safe_dump(
                safe({**resources, **nb['metadata']}), default_flow_style=False)
            nb['cells'].insert(
                0, __import__('nbformat').v4.new_markdown_cell("""---\n{}\n---\n""".format(source))
            )
            return nb, resources
```


<code>FrontMatter</code> appends the notebook metadata as a markdown cell at the beginning of the ntoebook.

    class FrontMatter(__import__('nbconvert').preprocessors.Preprocessor):
        def preprocess(self, nb, resources={}):
            source = __import__('yaml').safe_dump(
                safe({**resources, **nb['metadata']}), default_flow_style=False)
            nb['cells'].insert(
                0, __import__('nbformat').v4.new_markdown_cell("""---\n{}\n---\n""".format(source))
            )
            return nb, resources



```python
        exporter = __import__('nbconvert').get_exporter('markdown')(
            config={'TemplateExporter': {'preprocessors': [FrontMatter]}})
```


        exporter = __import__('nbconvert').get_exporter('markdown')(
            config={'TemplateExporter': {'preprocessors': [FrontMatter]}})



```python
---

> The snippet below shows the composed code.

<pre><code>{{o and exporter.from_filename('2017-06-24-Front-Matter-Preprocessor.ipynb')[0].lstrip()}}</code></pre>
```


---

> The snippet below shows the composed code.

<pre><code>---
description: Notebook metadata as front matter.
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
layout: post
metadata:
  modified_date: July 4, 2017
  name: 2017-06-24-Front-Matter-Preprocessor
  path: ''
output_extension: .md
outputs: {}

---


# Front Matter `nbconvert` preprocessor

Append *metadata* and *resources* as front matter to a notebook; insert a markdown cell at the beginning of notebook.


```python
    o = __name__ == '__main__'
    if o:
        %reload_ext literacy
```


```python
<code>safe</code> will make sure all Mapping objects are pure python __dict__

    def safe(object):
        if hasattr(object, 'items'):
            object = dict(object)
            for key, value in object.items():
                object.update({key: safe(value)})
        return object
```


<code>safe</code> will make sure all Mapping objects are pure python __dict__

    def safe(object):
        if hasattr(object, 'items'):
            object = dict(object)
            for key, value in object.items():
                object.update({key: safe(value)})
        return object



```python
<code>FrontMatter</code> appends the notebook metadata as a markdown cell at the beginning of the ntoebook.

    class FrontMatter(__import__('nbconvert').preprocessors.Preprocessor):
        def preprocess(self, nb, resources={}):
            source = __import__('yaml').safe_dump(
                safe({**resources, **nb['metadata']}), default_flow_style=False)
            nb['cells'].insert(
                0, __import__('nbformat').v4.new_markdown_cell("""---\n{}\n---\n""".format(source))
            )
            return nb, resources
```


<code>FrontMatter</code> appends the notebook metadata as a markdown cell at the beginning of the ntoebook.

    class FrontMatter(__import__('nbconvert').preprocessors.Preprocessor):
        def preprocess(self, nb, resources={}):
            source = __import__('yaml').safe_dump(
                safe({**resources, **nb['metadata']}), default_flow_style=False)
            nb['cells'].insert(
                0, __import__('nbformat').v4.new_markdown_cell("""---\n{}\n---\n""".format(source))
            )
            return nb, resources



```python
        exporter = __import__('nbconvert').get_exporter('markdown')(
            config={'TemplateExporter': {'preprocessors': [FrontMatter]}})
```


        exporter = __import__('nbconvert').get_exporter('markdown')(
            config={'TemplateExporter': {'preprocessors': [FrontMatter]}})



```python
---

> The snippet below shows the composed code.

<pre><code>{{o and exporter.from_filename('2017-06-24-Front-Matter-Preprocessor.ipynb')[0].lstrip()}}</code></pre>
```


---

> The snippet below shows the composed code.

<pre><code>---
description: Notebook metadata as front matter.
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
  modified_date: June 28, 2017
  name: 2017-06-24-Front-Matter-Preprocessor
  path: ''
output_extension: .md
outputs: {}

---


# Front Matter `nbconvert` preprocessor

Append *metadata* and *resources* as front matter to a notebook; insert a markdown cell at the beginning of notebook.


```python
o = __name__ == '__main__'
if o:
    %reload_ext literacy.template
```


```python
<code>safe</code> will make sure all Mapping objects are pure python __dict__

    def safe(object):
        if hasattr(object, 'items'):
            object = dict(object)
            for key, value in object.items():
                object.update({key: safe(value)})
        return object
```


<code>safe</code> will make sure all Mapping objects are pure python __dict__

    def safe(object):
        if hasattr(object, 'items'):
            object = dict(object)
            for key, value in object.items():
                object.update({key: safe(value)})
        return object



```python
<code>FrontMatter</code> appends the notebook metadata as a markdown cell at the beginning of the ntoebook.

    class FrontMatter(__import__('nbconvert').preprocessors.Preprocessor):
        def preprocess(self, nb, resources={}):
            source = __import__('yaml').safe_dump(
                safe({**resources, **nb['metadata']}), default_flow_style=False)
            nb['cells'].insert(
                0, __import__('nbformat').v4.new_markdown_cell("""---\n{}\n---\n""".format(source))
            )
            return nb, resources
```


<code>FrontMatter</code> appends the notebook metadata as a markdown cell at the beginning of the ntoebook.

    class FrontMatter(__import__('nbconvert').preprocessors.Preprocessor):
        def preprocess(self, nb, resources={}):
            source = __import__('yaml').safe_dump(
                safe({**resources, **nb['metadata']}), default_flow_style=False)
            nb['cells'].insert(
                0, __import__('nbformat').v4.new_markdown_cell("""---\n{}\n---\n""".format(source))
            )
            return nb, resources



```python
exporter = __import__('nbconvert').get_exporter('markdown')(
    config={'TemplateExporter': {'preprocessors': ['literacy.preprocessors.Dedent', FrontMatter]}})
```


        exporter = __import__('nbconvert').get_exporter('markdown')(
            config={'TemplateExporter': {'preprocessors': ['literacy.preprocessors.Dedent', FrontMatter]}})



```python
---

> The snippet below shows the composed code.

<pre><code>{{o and exporter.from_filename('2017-06-24-Front-Matter-Preprocessor.ipynb')[0].lstrip()}}</code></pre>
```

__normalize__ all the values of a collection to a basic `dict` type for `yaml.safe_load` to consume.
</code></pre><p><strong>normalize</strong> all the values of a collection to a basic <code>dict</code> type for <code>yaml.safe_load</code> to consume.
&lt;/code&gt;&lt;/pre&gt;</p>

<pre><code>---------------------------------------------------------------------------

NameError                                 Traceback (most recent call last)

&lt;ipython-input-5-06faa1d75631&gt; in &lt;module&gt;()
----&gt; 1 nbconvert


NameError: name 'nbconvert' is not defined


</code></pre>
<p><strong>normalize</strong> all the values of a collection to a basic <code>dict</code> type for <code>yaml.safe_load</code> to consume.
&lt;/code&gt;&lt;/pre&gt;</p>

</div>


      File "<ipython-input-5-e47d0e1bf424>", line 6
        ```python
        ^
    SyntaxError: invalid syntax


__normalize__ all the values of a collection to a basic `dict` type for `yaml.safe_load` to consume.
