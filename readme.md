---
anaconda-cloud: {}
config_dir: /Users/tonyfast/.jupyter
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
  name: readme
  path: ''
output_extension: .md
output_files_dir: readme_files
unique_key: readme

---

`foreverwhatever.github.io` is Tony Fast's personal journal of computational documents.


```python

```

<div class="output_markdown rendered_html output_subarea ">

<pre><code>    %load_ext literacy.template</code></pre>

</div>

---
    The literacy.template extension is already loaded. To reload it, use:
      %reload_ext literacy.template

---


```python

```

<div class="output_markdown rendered_html output_subarea ">
<h2 id="The-build-branch">The <strong>build</strong> branch<a class="anchor-link" href="#The-build-branch">&#182;</a></h2><p>The <strong>build</strong> branch uses <strong>travis-ci</strong> to transpile notebooks to a jekyll site on the <strong>master</strong> 
branch.  When <strong>master</strong> updates, the standard github pages <strong>jekyll</strong> build is used.</p>
<h3 id="A-collection-of-notebooks">A collection of notebooks<a class="anchor-link" href="#A-collection-of-notebooks">&#182;</a></h3><p>Create a collection of <strong>_notebooks</strong>. It folder is the source of <strong>markdown</strong>, <strong>json</strong>, and
<strong>python</strong> copies of the collection.</p>

</div>


```python

```

<div class="output_markdown rendered_html output_subarea ">
<h3 id="Python">Python<a class="anchor-link" href="#Python">&#182;</a></h3><p>The python <strong>nbconvert</strong> configuration is <em>_layouts/python.py</em>.  The module is in a <em>non</em>-<strong>Jekyll</strong> namespace;
I personally chose <strong>whatever</strong>.</p>

<pre><code>        !jupyter nbconvert --config _layouts/python.py --output-dir=whatever _notebooks/*.ipynb</code></pre>

</div>

---
    [NbConvertApp] Converting notebook _notebooks/2017-01-01-triangles.ipynb to python
    [NbConvertApp] Writing 521 bytes to whatever/2017-01-01-triangles.py
    [NbConvertApp] Converting notebook _notebooks/2017-06-24-Front-Matter-Preprocessor.ipynb to python
    [NbConvertApp] Writing 1379 bytes to whatever/2017-06-24-Front-Matter-Preprocessor.py
    [NbConvertApp] Converting notebook _notebooks/dummy.ipynb to python
    [NbConvertApp] Writing 521 bytes to whatever/dummy.py

---


```python

```

<div class="output_markdown rendered_html output_subarea ">
<h3 id="Markdown">Markdown<a class="anchor-link" href="#Markdown">&#182;</a></h3><p>The markdown <strong>nbconvert</strong> configuration is <em>_layouts/markdown.py</em></p>

<pre><code>!jupyter nbconvert --to markdown --config _layouts/markdown.py readme.ipynb

</code></pre>
<ul>
<li><p>Notebooks beginning with <strong>Numbers</strong> are inferred as <strong>_posts</strong></p>

<pre><code>  !jupyter nbconvert --to markdown --config _layouts/markdown.py --output-dir _posts _notebooks/[0-9]*.ipynb</code></pre>
</li>
<li><p>Notebooks beginning with <strong>Letters</strong> are inferred as <strong>_docs</strong></p>

<pre><code>  !jupyter nbconvert --to markdown --config _layouts/markdown.py --output-dir _docs _notebooks/[a-z,A-Z]*.ipynb</code></pre>
</li>
</ul>

</div>

---
    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Writing 1491 bytes to readme.md
    [NbConvertApp] Converting notebook _notebooks/2017-01-01-triangles.ipynb to markdown
    [NbConvertApp] Writing 716 bytes to _posts/2017-01-01-triangles.md
    [NbConvertApp] Converting notebook _notebooks/2017-06-24-Front-Matter-Preprocessor.ipynb to markdown
    [NbConvertApp] Writing 1110 bytes to _posts/2017-06-24-Front-Matter-Preprocessor.md
    [NbConvertApp] Converting notebook _notebooks/dummy.ipynb to markdown
    [NbConvertApp] Writing 671 bytes to _docs/dummy.md

---


```python

```

<div class="output_markdown rendered_html output_subarea ">
<h3 id="Data">Data<a class="anchor-link" href="#Data">&#182;</a></h3><p>The data <strong>nbconvert</strong> configuration is <em>_layouts/data.py</em></p>

<pre><code>        !jupyter nbconvert --to notebook --config _layouts/data.py _notebooks/*.ipynb</code></pre>

</div>

---
    [NbConvertApp] Converting notebook _notebooks/2017-01-01-triangles.ipynb to notebook
    [NbConvertApp] Writing 1628 bytes to _data/2017-01-01-triangles.json
    [NbConvertApp] Converting notebook _notebooks/dummy.ipynb to notebook
    [NbConvertApp] Writing 1628 bytes to _data/dummy.json

---
