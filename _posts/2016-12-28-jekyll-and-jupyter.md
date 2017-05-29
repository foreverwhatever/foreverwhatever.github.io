---
layout: post
modified_date: May 29, 2017
name: 2016-12-28-jekyll-and-jupyter
path: whatever

description: two templates to rule them all.
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
title: '`jupyter nbconvert` & `jekyll`'

---


# {{page.title}}

> Undoubtedly, `jupyter` is my favorite tool for innovation. And, `jekyll` is my most trusted open source resource.  This blog post combines the `jekyll` static sites to blog with `jupyter` notebooks & create reusable code during live document development.

---

        {% raw %}

## `templates`

`templates` weave variables of data with strings.  There are __<del>two</del>__ templating steps required to combine `jupyter` `notebook`s with the static site generator - `jekyll`.  The templates will

❶ convert a __notebook__ to markdown with `nbconvert`;  `python` templating package `jinja2` to transforms them from `ipynb`👉`md`

❷ `jekyll` will compile `liquid` before creating the static asset in `_site` - `md`👉`html`

## ❶ the `nbconvert` template

`_layouts` is the preferred `jekyll` directory for document level templates; this same directory will be used for `jinja2` templates and the `nbconvert` configuration files.

`_layouts/jekyll.md.tpl` is our ❶st template, it extends [`nbconvert.templates.markdown`](https://github.com/jupyter/nbconvert/blob/master/nbconvert/templates/markdown.tpl)


```python
        %%file ../_layouts/jekyll.md.tpl
        {% extends 'markdown.tpl' %}
```

---
    Overwriting ../_layouts/jekyll.md.tpl

---

#### frontmatter & `jekyll`

`jekyll` recognizes files beginning with `--- yaml: front matter ---`.  `nbconvert` will prepend the front matter and  markdownify the notebook.  The transformed file will be used by the `jekyll` server to create a static site.

Structured data in the `front matter` can be reused when `jekyll` renders the document.  The `nbconvert` template will contain the `notebook` metadata to the front matter.  It is preferrable for the `front matter` to be a `yaml` formatted string because it is easy to edit. 

> the `json.dump` - `json.load` - `yaml.safe_load` chain stringifies the notebook `metadata`


```python
        %%file ../_layouts/jekyll.md.tpl -a
        {%- block header scoped-%}
        ---
        layout: post
        {{ resources.metadata | dump | load | yaml(default_flow_style=False)}}
        {{ nb.metadata | dump | load | yaml(default_flow_style=False)}}
        ---
        {{super()}}
        {% endblock header %}
```

---
    Appending to ../_layouts/jekyll.md.tpl

---

> `layout: post` in the beginning is overridden `layout` in the notebook metadata.

###  template & outputs

####  `stream`

The standard python output - `stream` - should be notably separate from the inputs when we have viewers 👀 on the document.  Add horizontal rules to the `stream` block to delimit input and output cells.


```python
        %%file ../_layouts/jekyll.md.tpl -a
        {% block stream %}
        ---
        {{ output.text | indent }}
        ---
        {% endblock stream %}
```

---
    Appending to ../_layouts/jekyll.md.tpl

---

#### rich outputs

The standard `markdown` template will suppress rich display `block`s, unlike the `html/basic` template.  The snippet below copies the `data_*` blocks from the [`nbconvert.template.html.basic`](https://github.com/jupyter/nbconvert/blob/master/nbconvert/templates/html/basic.tpl) `template` to the `_layouts/jekyll.md.tpl`.


```python
        import jinja2; token = "{% block "
        env = jinja2.Environment(loader=jinja2.PackageLoader('nbconvert', 'templates/html'))
        with open('../_layouts/jekyll.md.tpl', 'a') as f:
            f.write('\n'.join([
                token + block
                for block in env.loader.get_source(env, 'basic.tpl')[0].split(token)[1:]
                if block.startswith('data_') and not block.startswith('data_priority')
            ]))
```

> Now images and javascript will embed into `markdown`.

### configuring `nbconvert`

Combining `jupyter` and `jekyll` requires a bit of customization.  `nbconvert`'s rich configuration system provides control when transforming `ipynb` files to other formats. 

> the `py🐍hon` configuration file for the `markdown/jekyll` hybrid is [`_layouts/markdown.py`]().

Our configuration file exports `markdown` files to the `_posts` directory using the template `_layouts/jekyll.md.tpl`.


```python
        %%file ../_layouts/markdown.py
        c.NbConvertApp.export_format = 'markdown'
        c.FilesWriter.build_directory = '_posts'
        c.TemplateExporter.template_file = '_layouts/jekyll.md.tpl';
```

---
    Overwriting ../_layouts/markdown.py

---

#### filters

`jinja2` provides filters to manipulate `python` objects before finally becoming a string; this action is not easily reversible.  There are some native `nbconvert` filters like `indent` are used in `block stream`.  In the `front matter` we join `dump | load | yaml` to format our `front matter`.  The snippet below assigns these filters to the using their qualified `python` import path


```python
        %%file ../_layouts/markdown.py -a
        c.TemplateExporter.filters = {'dump': 'json.dumps', 'load': 'json.loads', 'yaml': 'yaml.dump'};
```

---
    Appending to ../_layouts/markdown.py

---

#### `display_priority`

`nbconvert` natively decouples images from a notebook & does not template javascript.  The modification to the configuration below makes sure images are embedded as is the javascript.


```python
        %%file ../_layouts/markdown.py -a
        c.ExtractOutputPreprocessor.enabled=False;
        c.NbConvertBase.display_data_priority = ['text/html', 'text/markdown', 'image/svg+xml', 'text/latex', 'image/png', 'image/jpeg', 'text/plain', 'application/javascript']
```

---
    Appending to ../_layouts/markdown.py

---

## ❷ the `jekyll` `_layout`


```python
        import bs4, nbformat, nbconvert
```

`_layouts/jekyll.md.tpl` formats a notebook as `markdown`.  It is reasonable to go directly to `html`, but that may limit the ability to edit the post later on.  The alternative will nest the `markdown` into an `html` template containing all of the notebook `style`.  The `html` template will be placed in `_layouts/post.html`.

#### `post` template

Start with this `notebook`


```python
        post = '2015-12-28-jekyll-and-jupyter.ipynb'
```

& convert it to a `BeautifulSoup` object with the `nbconvert.templates.html.full` template.


```python
        body = nbconvert.export(
            nbconvert.get_exporter('html'), nbformat.read(post, 4))[0]
        soup = bs4.BeautifulSoup(body, 'lxml')
```

Create `div#notebook-container`


```python
        div = soup.new_tag('div', id='notebook-container', **{'class': "container"})        
```

`jekyll` places  blocks in the `_includes` directory.  For example, `_includes/disqus.html` will append `Disqus` comments to each post


```python
        div.append('{'+'{content}}')
        div.append('{'+'% include disqus.html %}')
```

Replace the body of this `notebook` with `div#notebook-container` and prepend a block for navigation.


```python
        soup.select_one('#notebook-container').replace_with(div)
        soup.select_one('#notebook-container').insert_before('{% include header.html %}')
```

---


```python
        with "💾" and open('../_layouts/post.html', 'w') as f: f.write(str(soup))
```

## conversion

Use the `jupyter nbconvert` CLI to convert the notebook 👉 `markdown` in `_posts`.


```python
        !time jupyter nbconvert --config ../_layouts/markdown.py --output-dir ../_posts --template ../_layouts/jekyll.md.tpl 2015-12-28-jekyll-and-jupyter.ipynb
```

---
    [NbConvertApp] Converting notebook 2015-12-28-jekyll-and-jupyter.ipynb to markdown
    [NbConvertApp] Writing 8739 bytes to ../_posts/2015-12-28-jekyll-and-jupyter.md
    
    real	0m0.952s
    user	0m0.855s
    sys	0m0.081s

---

## other

* __`nbconvert` command line config__ Is it possible to supply a `dict` on the command line, like `TemplateExporter.filters`?

* __Why `yaml`?__ `yaml` is the easiest way to edit `json`.

* __Why `jekyll` for static sites?__ `jekyll` provides predictable deployment on Github with `pages`.
