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
  modified_date: July 31, 2017
  name: readme
  path: ''
output_extension: .md
output_files_dir: readme_files
unique_key: readme

---

`foreverwhatever.github.io` is Tony Fast's personal journal of computational documents.



<div class="output_markdown rendered_html output_subarea ">
<h2 id="The-build-branch">The <strong>build</strong> branch<a class="anchor-link" href="#The-build-branch">&#182;</a></h2><p>The <strong>build</strong> branch uses <strong>travis-ci</strong> to transpile notebooks to a jekyll site on the <strong>master</strong> 
branch.  When <strong>master</strong> updates, the standard github pages <strong>jekyll</strong> build is used.</p>
<h3 id="A-collection-of-notebooks">A collection of notebooks<a class="anchor-link" href="#A-collection-of-notebooks">&#182;</a></h3><p>Create a collection of <strong>_notebooks</strong>. It folder is the source of <strong>markdown</strong>, <strong>json</strong>, and
<strong>python</strong> copies of the collection.</p>

</div>


<div class="output_markdown rendered_html output_subarea ">
<h3 id="Markdown">Markdown<a class="anchor-link" href="#Markdown">&#182;</a></h3><ul>
<li><p>The markdown <strong>nbconvert</strong> configuration is <em>_layouts/markdown.py</em></p>

<pre><code>  !jupyter nbconvert --to html --config _layouts/markdown.py index.ipynb</code></pre>
</li>
<li><p>The markdown <strong>nbconvert</strong> configuration is <em>_layouts/markdown.py</em></p>

<pre><code>  !jupyter nbconvert --to markdown --config _layouts/markdown.py readme.ipynb</code></pre>
</li>
<li><p>Notebooks beginning with <strong>Numbers</strong> are inferred as <strong>_posts</strong></p>

<pre><code>  !jupyter nbconvert --to markdown --config _layouts/markdown.py --output-dir _posts whatever/[0-9]*.ipynb</code></pre>
</li>
<li><p>Notebooks beginning with <strong>Letters</strong> are inferred as <strong>_docs</strong></p>

<pre><code>  !jupyter nbconvert --to markdown --config _layouts/markdown.py --output-dir _docs whatever/[a-z,A-Z]*.ipynb</code></pre>
</li>
</ul>

</div>

---
[NbConvertApp] Converting notebook index.ipynb to html
Traceback (most recent call last):
  File "/Users/tonyfast/anaconda/bin/jupyter-nbconvert", line 6, in <module>
    sys.exit(nbconvert.nbconvertapp.main())
  File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/jupyter_core/application.py", line 267, in launch_instance
    return super(JupyterApp, cls).launch_instance(argv=argv, **kwargs)
  File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/traitlets/config/application.py", line 658, in launch_instance
    app.start()
  File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/nbconvertapp.py", line 313, in start
    self.convert_notebooks()
  File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/nbconvertapp.py", line 481, in convert_notebooks
    self.convert_single_notebook(notebook_filename)
  File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/nbconvertapp.py", line 452, in convert_single_notebook
    output, resources = self.export_single_notebook(notebook_filename, resources, input_buffer=input_buffer)
  File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/nbconvertapp.py", line 381, in export_single_notebook
    output, resources = self.exporter.from_filename(notebook_filename, resources=resources)
  File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/exporters/exporter.py", line 172, in from_filename
    return self.from_file(f, resources=resources, **kw)
  File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/exporters/exporter.py", line 190, in from_file
    return self.from_notebook_node(nbformat.read(file_stream, as_version=4), resources=resources, **kw)
  File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/exporters/html.py", line 84, in from_notebook_node
    return super(HTMLExporter, self).from_notebook_node(nb, resources, **kw)
  File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/exporters/templateexporter.py", line 283, in from_notebook_node
    output = self.template.render(nb=nb_copy, resources=resources)
  File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/jinja2/environment.py", line 1008, in render
    return self.environment.handle_exception(exc_info, True)
  File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "/Users/tonyfast/foreverwhatever.github.io/_layouts/jekyll.md.tpl", line 1, in top-level template code
    {% extends 'markdown.tpl' %}
jinja2.exceptions.TemplateNotFound: markdown.tpl
[NbConvertApp] Converting notebook readme.ipynb to markdown
[NbConvertApp] Writing 11526 bytes to readme.md
[NbConvertApp] Converting notebook whatever/2017-06-24-Front-Matter-Preprocessor.ipynb to markdown
[NbConvertApp] Writing 12046 bytes to _posts/2017-06-24-Front-Matter-Preprocessor.md
[NbConvertApp] Converting notebook whatever/2017-06-25-Preprocessor.ipynb to markdown
[NbConvertApp] Writing 3693 bytes to _posts/2017-06-25-Preprocessor.md
[NbConvertApp] Converting notebook whatever/2017-06-28-Add-Cells-With-Code.ipynb to markdown
[NbConvertApp] Writing 773 bytes to _posts/2017-06-28-Add-Cells-With-Code.md
[NbConvertApp] Converting notebook whatever/2017-06-29-GridPlot-In-Bokeh.ipynb to markdown
[NbConvertApp] Writing 119177 bytes to _posts/2017-06-29-GridPlot-In-Bokeh.md
[NbConvertApp] Converting notebook whatever/2017-07-02-Sierpinski triangle in Bokeh.ipynb to markdown
[NbConvertApp] Writing 2227292 bytes to _posts/2017-07-02-Sierpinski triangle in Bokeh.md
[NbConvertApp] Converting notebook whatever/2017-07-06-The-Alphabet-Cipher.ipynb to markdown
[NbConvertApp] Writing 4532 bytes to _posts/2017-07-06-The-Alphabet-Cipher.md
[NbConvertApp] Converting notebook whatever/2017-07-16-JSON-patch-Jupyter-Notebooks.ipynb to markdown
[NbConvertApp] Writing 58039 bytes to _posts/2017-07-16-JSON-patch-Jupyter-Notebooks.md
[NbConvertApp] Converting notebook whatever/2017-07-20-Spinning-Pie.ipynb to markdown
[NbConvertApp] Writing 34422 bytes to _posts/2017-07-20-Spinning-Pie.md
[NbConvertApp] Converting notebook whatever/gridplot-Copy1.ipynb to markdown
[NbConvertApp] Writing 69809 bytes to _docs/gridplot-Copy1.md
[NbConvertApp] Converting notebook whatever/gridplot-Copy2.ipynb to markdown
[NbConvertApp] Writing 102579 bytes to _docs/gridplot-Copy2.md
[NbConvertApp] Converting notebook whatever/gridplot-Copy3.ipynb to markdown
[NbConvertApp] Writing 5966 bytes to _docs/gridplot-Copy3.md
[NbConvertApp] Converting notebook whatever/gridplot-Copy4.ipynb to markdown
[NbConvertApp] Writing 500 bytes to _docs/gridplot-Copy4.md
[NbConvertApp] Converting notebook whatever/gridplot.ipynb to markdown
[NbConvertApp] Writing 1362251 bytes to _docs/gridplot.md

---

