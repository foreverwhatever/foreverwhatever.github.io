---
anaconda-cloud: {}
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
<<<<<<< Updated upstream
  modified_date: July 23, 2017
=======
  modified_date: July 31, 2017
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
=======
<pre><code>  !jupyter nbconvert --to html --config _layouts/markdown.py index.ipynb</code></pre>
</li>
<li><p>The markdown <strong>nbconvert</strong> configuration is <em>_layouts/markdown.py</em></p>

>>>>>>> Stashed changes
<pre><code>  !jupyter nbconvert --to markdown --config _layouts/markdown.py readme.ipynb</code></pre>
</li>
<li><p>Notebooks beginning with <strong>Numbers</strong> are inferred as <strong>_posts</strong></p>

<pre><code>  !jupyter nbconvert --to markdown --config _layouts/markdown.py --output-dir _posts whatever/[0-9]*.ipynb</code></pre>
</li>
<li><p>Notebooks beginning with <strong>Letters</strong> are inferred as <strong>_docs</strong></p>

<pre><code>  # !jupyter nbconvert --to markdown --config _layouts/markdown.py --output-dir _docs whatever/[a-z,A-Z]*.ipynb</code></pre>
</li>
</ul>

</div>

---
<<<<<<< Updated upstream
[NbConvertApp] Converting notebook readme.ipynb to markdown
[NbConvertApp] Writing 2191 bytes to readme.md
[NbConvertApp] Converting notebook whatever/2017-06-24-Front-Matter-Preprocessor.ipynb to markdown
[NbConvertApp] Writing 12045 bytes to _posts/2017-06-24-Front-Matter-Preprocessor.md
[NbConvertApp] Converting notebook whatever/2017-06-25-Preprocessor.ipynb to markdown
[NbConvertApp] Writing 3693 bytes to _posts/2017-06-25-Preprocessor.md
[NbConvertApp] Converting notebook whatever/2017-06-28-Add-Cells-With-Code.ipynb to markdown
[NbConvertApp] Writing 773 bytes to _posts/2017-06-28-Add-Cells-With-Code.md
[NbConvertApp] Converting notebook whatever/2017-06-29-GridPlot-In-Bokeh.ipynb to markdown
[NbConvertApp] Writing 123163 bytes to _posts/2017-06-29-GridPlot-In-Bokeh.md
[NbConvertApp] Converting notebook whatever/2017-07-02-Sierpinski triangle in Bokeh.ipynb to markdown
[NbConvertApp] Writing 2227292 bytes to _posts/2017-07-02-Sierpinski triangle in Bokeh.md
=======
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
<<<<<<< HEAD
[NbConvertApp] Writing 7856 bytes to readme.md
[NbConvertApp] Converting notebook whatever/2017-06-24-Front-Matter-Preprocessor.ipynb to markdown
[NbConvertApp] Writing 5362 bytes to _posts/2017-06-24-Front-Matter-Preprocessor.md
[NbConvertApp] Converting notebook whatever/2017-06-25-Preprocessor.ipynb to markdown
[NbConvertApp] Writing 3693 bytes to _posts/2017-06-25-Preprocessor.md
[NbConvertApp] Converting notebook whatever/2017-06-28-Add-Cells-With-Code.ipynb to markdown
[NbConvertApp] Writing 2677 bytes to _posts/2017-06-28-Add-Cells-With-Code.md
[NbConvertApp] Converting notebook whatever/2017-06-29-GridPlot-In-Bokeh.ipynb to markdown
[NbConvertApp] Writing 119160 bytes to _posts/2017-06-29-GridPlot-In-Bokeh.md
[NbConvertApp] WARNING | pattern 'whatever/[a-z,A-Z]*.ipynb' matched no files
This application is used to convert notebook files (*.ipynb) to various other
formats.

WARNING: THE COMMANDLINE INTERFACE MAY CHANGE IN FUTURE RELEASES.

Options
-------

Arguments that take values are actually convenience aliases to full
Configurables, whose aliases are listed on the help line. For more information
on full configurables, see '--help-all'.

--allow-errors
    Continue notebook execution even if one of the cells throws an error and include the error message in the cell output (the default behaviour is to abort conversion). This flag is only relevant if '--execute' was specified, too.
--stdout
    Write notebook output to stdout instead of files.
--no-prompt
    Exclude input and output prompts from converted document.
--execute
    Execute the notebook prior to export.
-y
    Answer yes to any questions instead of prompting.
--debug
    set log level to logging.DEBUG (maximize logging output)
--inplace
    Run nbconvert in place, overwriting the existing notebook (only 
    relevant when converting to notebook format)
--generate-config
    generate default config file
--stdin
    read a single notebook file from stdin. Write the resulting notebook with default basename 'notebook.*'
--reveal-prefix=<Unicode> (SlidesExporter.reveal_url_prefix)
    Default: ''
    The URL prefix for reveal.js. This can be a a relative URL for a local copy
    of reveal.js, or point to a CDN.
    For speaker notes to work, a local reveal.js prefix must be used.
--template=<Unicode> (TemplateExporter.template_file)
    Default: ''
    Name of the template file to use
--post=<DottedOrNone> (NbConvertApp.postprocessor_class)
    Default: ''
    PostProcessor class used to write the results of the conversion
--nbformat=<Enum> (NotebookExporter.nbformat_version)
    Default: 4
    Choices: [1, 2, 3, 4]
    The nbformat version to write. Use this to downgrade notebooks.
--to=<Unicode> (NbConvertApp.export_format)
    Default: 'html'
    The export format to be used, either one of the built-in formats, or a
    dotted object name that represents the import path for an `Exporter` class
--writer=<DottedObjectName> (NbConvertApp.writer_class)
    Default: 'FilesWriter'
    Writer class used to write the  results of the conversion
--output-dir=<Unicode> (FilesWriter.build_directory)
    Default: ''
    Directory to write output(s) to. Defaults to output to the directory of each
    notebook. To recover previous default behaviour (outputting to the current
    working directory) use . as the flag value.
--config=<Unicode> (JupyterApp.config_file)
    Default: ''
    Full path of a config file.
--output=<Unicode> (NbConvertApp.output_base)
    Default: ''
    overwrite base name use for output files. can only be used when converting
    one notebook at a time.
--log-level=<Enum> (Application.log_level)
    Default: 30
    Choices: (0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL')
    Set the log level by value or name.

To see all available configurables, use `--help-all`

Examples
--------

    The simplest way to use nbconvert is
    
    > jupyter nbconvert mynotebook.ipynb
    
    which will convert mynotebook.ipynb to the default format (probably HTML).
    
    You can specify the export format with `--to`.
    Options include ['asciidoc', 'custom', 'html', 'latex', 'markdown', 'notebook', 'pdf', 'python', 'rst', 'script', 'slides']
    
    > jupyter nbconvert --to latex mynotebook.ipynb
    
    Both HTML and LaTeX support multiple output templates. LaTeX includes
    'base', 'article' and 'report'.  HTML includes 'basic' and 'full'. You
    can specify the flavor of the format used.
    
    > jupyter nbconvert --to html --template basic mynotebook.ipynb
    
    You can also pipe the output to stdout, rather than a file
    
    > jupyter nbconvert mynotebook.ipynb --stdout
    
    PDF is generated via latex
    
    > jupyter nbconvert mynotebook.ipynb --to pdf
    
    You can get (and serve) a Reveal.js-powered slideshow
    
    > jupyter nbconvert myslides.ipynb --to slides --post serve
    
    Multiple notebooks can be given at the command line in a couple of 
    different ways:
    
    > jupyter nbconvert notebook*.ipynb
    > jupyter nbconvert notebook1.ipynb notebook2.ipynb
    
    or you can specify the notebooks list in a config file, containing::
    
        c.NbConvertApp.notebooks = ["my_notebook.ipynb"]
    
    > jupyter nbconvert --config mycfg.py

=======
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
>>>>>>> nbd
>>>>>>> Stashed changes

---

