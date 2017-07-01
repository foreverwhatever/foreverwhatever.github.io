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
  modified_date: June 30, 2017
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
<h3 id="Markdown">Markdown<a class="anchor-link" href="#Markdown">&#182;</a></h3><p>The markdown <strong>nbconvert</strong> configuration is <em>_layouts/markdown.py</em></p>

<pre><code>!jupyter nbconvert --to markdown --config _layouts/markdown.py readme.ipynb

</code></pre>
<ul>
<li><p>Notebooks beginning with <strong>Numbers</strong> are inferred as <strong>_posts</strong></p>

<pre><code>  !jupyter nbconvert --to markdown --config _layouts/markdown.py --output-dir _posts whatever/[0-9]*.ipynb</code></pre>
</li>
<li><p>Notebooks beginning with <strong>Letters</strong> are inferred as <strong>_docs</strong></p>

<pre><code>  !jupyter nbconvert --to markdown --config _layouts/markdown.py --output-dir _docs whatever/[a-z,A-Z]*.ipynb</code></pre>
</li>
</ul>

</div>

---
    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Writing 4607 bytes to readme.md
    [NbConvertApp] Converting notebook whatever/2017-06-24-Front-Matter-Preprocessor.ipynb to markdown
    [NbConvertApp] Writing 6797 bytes to _posts/2017-06-24-Front-Matter-Preprocessor.md
    [NbConvertApp] Converting notebook whatever/2017-06-25-Preprocessor.ipynb to markdown
    [NbConvertApp] Writing 5568 bytes to _posts/2017-06-25-Preprocessor.md
    [NbConvertApp] Converting notebook whatever/2017-06-28-Add-Cells-With-Code.ipynb to markdown
    [NbConvertApp] Writing 3583 bytes to _posts/2017-06-28-Add-Cells-With-Code.md
    [NbConvertApp] Converting notebook whatever/2017-06-29-GridPlot-In-Bokeh.ipynb to markdown
    [NbConvertApp] Writing 116587 bytes to _posts/2017-06-29-GridPlot-In-Bokeh.md
    [NbConvertApp] WARNING | pattern 'whatever/[a-z,A-Z]*.ipynb' matched no files
    This application is used to convert notebook files (*.ipynb) to various other
    formats.
    
    WARNING: THE COMMANDLINE INTERFACE MAY CHANGE IN FUTURE RELEASES.
    
    Options
    -------
    
    Arguments that take values are actually convenience aliases to full
    Configurables, whose aliases are listed on the help line. For more information
    on full configurables, see '--help-all'.
    
    --stdin
        read a single notebook file from stdin. Write the resulting notebook with default basename 'notebook.*'
    --debug
        set log level to logging.DEBUG (maximize logging output)
    --allow-errors
        Continue notebook execution even if one of the cells throws an error and include the error message in the cell output (the default behaviour is to abort conversion). This flag is only relevant if '--execute' was specified, too.
    -y
        Answer yes to any questions instead of prompting.
    --no-prompt
        Exclude input and output prompts from converted document.
    --generate-config
        generate default config file
    --inplace
        Run nbconvert in place, overwriting the existing notebook (only 
        relevant when converting to notebook format)
    --stdout
        Write notebook output to stdout instead of files.
    --execute
        Execute the notebook prior to export.
    --log-level=<Enum> (Application.log_level)
        Default: 30
        Choices: (0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL')
        Set the log level by value or name.
    --reveal-prefix=<Unicode> (SlidesExporter.reveal_url_prefix)
        Default: ''
        The URL prefix for reveal.js. This can be a a relative URL for a local copy
        of reveal.js, or point to a CDN.
        For speaker notes to work, a local reveal.js prefix must be used.
    --nbformat=<Enum> (NotebookExporter.nbformat_version)
        Default: 4
        Choices: [1, 2, 3, 4]
        The nbformat version to write. Use this to downgrade notebooks.
    --writer=<DottedObjectName> (NbConvertApp.writer_class)
        Default: 'FilesWriter'
        Writer class used to write the  results of the conversion
    --output=<Unicode> (NbConvertApp.output_base)
        Default: ''
        overwrite base name use for output files. can only be used when converting
        one notebook at a time.
    --to=<Unicode> (NbConvertApp.export_format)
        Default: 'html'
        The export format to be used, either one of the built-in formats, or a
        dotted object name that represents the import path for an `Exporter` class
    --template=<Unicode> (TemplateExporter.template_file)
        Default: ''
        Name of the template file to use
    --post=<DottedOrNone> (NbConvertApp.postprocessor_class)
        Default: ''
        PostProcessor class used to write the results of the conversion
    --output-dir=<Unicode> (FilesWriter.build_directory)
        Default: ''
        Directory to write output(s) to. Defaults to output to the directory of each
        notebook. To recover previous default behaviour (outputting to the current
        working directory) use . as the flag value.
    --config=<Unicode> (JupyterApp.config_file)
        Default: ''
        Full path of a config file.
    
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
    

---


<div class="output_markdown rendered_html output_subarea ">
<h3 id="Data">Data<a class="anchor-link" href="#Data">&#182;</a></h3><p>The data <strong>nbconvert</strong> configuration is <em>_layouts/data.py</em></p>

<pre><code>        # !jupyter nbconvert --to notebook --config _layouts/data.py _whatever/*.ipynb</code></pre>

</div>
