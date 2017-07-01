---
config_dir: /home/travis/.jupyter
description: Use the Jupyter Javascript API to append input cells.
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
  modified_date: July 1, 2017
  name: 2017-06-28-Add-Cells-With-Code
  path: whatever
output_extension: .md
output_files_dir: 2017-06-28-Add-Cells-With-Code_files
unique_key: 2017-06-28-Add-Cells-With-Code

---

I want to set multiple inputs in the Jupyter notebook.  

### Resources

* "Creating a new notebook cell from within a widget does not work"



<div class="output_markdown rendered_html output_subarea ">
<h2 id="Javascript">Javascript<a class="anchor-link" href="#Javascript">&#182;</a></h2><ul>
<li><p>The <code>next_input</code> is created using the <code>Jupyter</code> Javascript API.</p>

<pre><code>  next_input = """Jupyter.notebook.insert_cell_below(
      "code", Jupyter.notebook.get_selected_cells_indices()[0]
  ).set_text(atob("{}"))""".format</code></pre>
</li>
</ul>

</div>


<div class="output_markdown rendered_html output_subarea ">
<h2 id="Python">Python<a class="anchor-link" href="#Python">&#182;</a></h2>
<pre><code>    from IPython.display import Javascript, display
    from IPython.utils.py3compat import str_to_bytes, bytes_to_str
    from base64 import b64encode

</code></pre>
<p>Compose the <code>next_input</code> and display the Javascript.</p>

<pre><code>    def display_input(code):
        display(Javascript(next_input(bytes_to_str(b64encode(str_to_bytes(code))))))</code></pre>

</div>


<div class="output_markdown rendered_html output_subarea ">

<pre><code>    display_input('Set programmatically 💯')
    display_input('The computer seasdft this 🐢')</code></pre>

</div>


    <IPython.core.display.Javascript object>



    <IPython.core.display.Javascript object>











