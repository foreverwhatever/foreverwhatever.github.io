---
config_dir: /home/travis/.jupyter
description: A decorator to easily make nbconvert preprocessors.
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
  modified_date: July 2, 2017
  name: 2017-06-25-Preprocessor
  path: whatever
output_extension: .md
output_files_dir: 2017-06-25-Preprocessor_files
unique_key: 2017-06-25-Preprocessor

---

# A decorator to create nbconvert preprocessors.

This notebook makes it easier to create preprocessors for __nbconvert__.  These should work on an existing exporter.

* https://github.com/jupyter/nbconvert-examples/blob/master/custom_preprocessor/cheese_preprocessor.py
* http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html#function-decorators




<div class="output_markdown rendered_html output_subarea ">
<ul>
<li><p>There is a decorator that does that following</p>
<ul>
<li>Let's make a simple cell <code>from nbconvert.preprocessors import Preprocessor</code> that appends the cell index to the cell metadata.</li>
</ul>
</li>
</ul>

</div>


<div class="output_markdown rendered_html output_subarea ">
<p>The basic structure of <strong>SomeNewPreProcessor</strong> is:</p>

<pre><code>class SomeNewPreProcessor(Preprocessor): 
    def preprocess(self, nb, resources={}):
        return nb, resources

    def preprocess_cell(self, nb, resources, index):
        return nb, resources</code></pre>

</div>


<div class="output_markdown rendered_html output_subarea ">

<pre><code>import typing</code></pre>

</div>


<div class="output_markdown rendered_html output_subarea ">
<h2 id="The-@preprocess_cell-decorator">The <em>@preprocess_cell</em> decorator<a class="anchor-link" href="#The-@preprocess_cell-decorator">&#182;</a></h2>
<pre><code>def preprocess_cell(f: typing.Callable[[__import__("nbformat").NotebookNode, dict, int], Preprocessor]):
    return type(f.__name__, (Preprocessor, ), {"preprocess_cell": f})</code></pre>

</div>


<div class="output_markdown rendered_html output_subarea ">
<h3 id="The-NumberCell-example-&#128640;">The <em>NumberCell</em> example &#128640;<a class="anchor-link" href="#The-NumberCell-example-&#128640;">&#182;</a></h3><hr>
<p>Append the cell index to the cell metadata.</p>

<pre><code>@preprocess_cell
def NumberCell(self, cell, resources, index):
    cell['metadata'].update(index=index)
    return cell, resources</code></pre>

</div>


<div class="output_markdown rendered_html output_subarea ">
<h2 id="Test-NumberCell;">Test <code>NumberCell;</code><a class="anchor-link" href="#Test-NumberCell;">&#182;</a></h2>
<pre><code>from nbconvert import export, get_exporter

exporter = get_exporter('notebook')(config={
    'Exporter': {'preprocessors': [NumberCell]}})

#         print(exporter.from_filename('2017-06-25-Prepro.ipynb')[0])

</code></pre>
<hr>

</div>
# Lets make a config file

> <del>The code is commented out so the conversion works.</del>


<div class="output_markdown rendered_html output_subarea ">

<pre><code>#     %%file number.py
#     c.Exporter.preprocessors = ['whatever.2017-06-25-Preprocessor.NumberCell']</code></pre>

</div>


<div class="output_markdown rendered_html output_subarea ">

<pre><code>if o: 
    !jupyter nbconvert --to notebook --config number.py 2017-06-25-Preprocessor.ipynb</code></pre>

</div>

---
[NbConvertApp] Converting notebook 2017-06-25-Preprocessor.ipynb to notebook
[NbConvertApp] Writing 8091 bytes to 2017-06-25-Preprocessor.nbconvert.ipynb

---
