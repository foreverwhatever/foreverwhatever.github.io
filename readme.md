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
  modified_date: July 6, 2017
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

