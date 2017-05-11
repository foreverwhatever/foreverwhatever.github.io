
# {{page.title}}

{{data}}
---

> Undoubtedly, `jupyter` is my favorite tool for innovation. And, `jekyll` is my most trusted open source resource.  This blog post combines the `jekyll` static site & blogs with `jupyter` notebook namespaces for live document development.  

---

        {% raw %}

## `templates`

__<del>Two</del>__ templating steps are necessary to use `jupyter` `notebook`s with the static site generator `jekyll`.  The templates will

❶ convert a __notebook__ to markdown with `nbconvert` and `jinja2` templates

❷ `jekyll` will compile `liquid` before creating the static `_site`.

Throughout this `post`, we discuess __another__ conversion pipeline to blogging `jupyter` notebooks. 

## ❶ the `nbconvert` template

`_layouts` is the preferred `jekyll` directory for document level templates; this same directory will be used for `jinja2` templates and the `nbconvert` configuration files.

`_layouts/jekyll.md.tpl` extends the [`nbconvert.templates.markdown`](https://github.com/jupyter/nbconvert/blob/master/nbconvert/templates/markdown.tpl) `jinja2` template


```python
        %%file ../_layouts/jekyll.md.tpl
        {% extends 'markdown.tpl' %}
```

    Overwriting ../_layouts/jekyll.md.tpl


> `%%file ../_layouts/jekyll.md.tpl` cells create a template to convert `ipynb` 👉 `md`.

#### frontmatter & `jekyll`

`jekyll` recognizes files beginning with `--- front matter ---`.  `nbconvert` will markdownify the notebook and preprend the front matter.  The transformed file will be used by the `jekyll` server to create a static site.

Structured data in the `front matter` can be reused when `jekyll` renders the document.  The `nbconvert` template will prepend the notebook metadata to the front matter.  It is preferrable for the `front matter` to be a `yaml` formatted string. 

> `json.dump` | `json.load` | `yaml.safe_load` stringifies the notebook `metadata`


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

    Appending to ../_layouts/jekyll.md.tpl


##  outputs

The standard python output - `stream` - should be notably separate from the inputs when we have viewers 👀 on the document.  Add horizontal rules to the `stream` block to delimit input and output cells.

### `stream` and rich outputs

It is necessary to place `javascript` into the markdown files; I commonly use `bokeh` and `coffeescript` in notebook.  The `data_javascript` block is not defined for the `nbconvert.template.markdown`, but it is in [`nbconvert.template.html.basic`](https://github.com/jupyter/nbconvert/blob/master/nbconvert/templates/html/basic.tpl). 

> the snippet below is a verbatim [copy🍝](https://github.com/jupyter/nbconvert/blob/master/nbconvert/templates/html/basic.tpl#L212).


```python
        %%file ../_layouts/jekyll.md.tpl -a
        {% block stream %}
        ---
        {{ output.text | indent }}
        ---
        {% endblock stream %}
```

    Appending to ../_layouts/jekyll.md.tpl



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

* Add `application/javascript` to the display priority.

https://github.com/jupyter/nbconvert/blob/master/nbconvert/exporters/markdown.py#L36

## <small>❶</small> configuring `nbconvert`

Combining `jupyter` and `jekyll` requires a bit of customization.  `nbconvert`'s rich configuration system provides control when transforming `ipynb` files to other formats.  In this pipeline, we focus on converting `ipynb` files to `markdown` for a `jekyll` blog.

> the `py🐍hon` configuration file for the `markdown/jekyll` hybrid is [`_layouts/markdown.py`]().

#### filters

`jinja2` provides filters to manipulate `python` objects before finally becoming a string.  There are some native `nbconvert` filters like `indent` used in the `block stream`.  In the `front matter` we declare `| dump | load | yaml` to format our `front matter`.  The snippet below appends these filters to the 


```python
        %%file ../_layouts/markdown.py
        c.TemplateExporter.filters = {
            'dump': 'json.dumps',
            'load': 'json.loads',
            'yaml': 'yaml.dump'};
```

    Overwriting ../_layouts/markdown.py


##### embedding images

`nbconvert` natively extracts images from a notebook.  The setting below will leave images embedded.


```python
        %%file ../_layouts/markdown.py -a
        c.ExtractOutputPreprocessor.enabled=False;
```

    Appending to ../_layouts/markdown.py


### rich outputs

It is necessary to place `javascript` into the markdown files; I commonly use `bokeh` and `coffeescript` in notebook.  The `data_javascript` block is not defined for the `nbconvert.template.markdown`, but it is in [`nbconvert.template.html.basic`](https://github.com/jupyter/nbconvert/blob/master/nbconvert/templates/html/basic.tpl). 

> the snippet below is a verbatim [copy🍝](https://github.com/jupyter/nbconvert/blob/master/nbconvert/templates/html/basic.tpl#L212).


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

* Add `application/javascript` to the display priority.

https://github.com/jupyter/nbconvert/blob/master/nbconvert/exporters/markdown.py#L36


```python
        %%file ../_layouts/markdown.py -a
        c.NbConvertBase.display_data_priority = ['text/html', 'text/markdown', 'image/svg+xml', 'text/latex', 'image/png', 'image/jpeg', 'text/plain', 'application/javascript']
```

    Appending to ../_layouts/markdown.py


## ❷ the `jekyll` `_layout`


```python
import bs4, nbformat, nbconvert
```

`_layouts/jekyll.md.tpl` formats a notebook as `markdown`.  It is reasonable to go directly to `html`, but that may limit the ability to edit the post later on.  The alternative will nest the `markdown` into an `html` template containing all of the notebook `style`.  The `html` template will be placed in `_layouts/post.html`.

#### `post` template

Start with this `notebook`


```python
        post = '2015-12-27-jekyll-and-jupyter.ipynb'
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

& append the `markdown` post content


```python
        div.append('{{content}}')
```

`jekyll` places  blocks in the `_includes` directory.  For example, `_includes/disqus.html` will append `Disqus` comments to each post


```python
#         div.append('{% include disqus.html %}')
```

Replace the body of this `notebook` with `div#notebook-container`


```python
        soup.select_one('#notebook-container').replace_with(div);
```

Prepend a `block` for navigation & save the template.


```python
        soup.select_one('#notebook-container').insert_before('{% include header.html %}')
        with open('../_layouts/post.html', 'w') as f: f.write(str(soup))
```


```python
        !jupyter nbconvert --to markdown --config ../_
```

## other

* __`nbconvert` command line config__ Is it possible to supply a `dict` on the command line, like `TemplateExporter.filters`?

* __Why `yaml`?__ `yaml` is the easiest way to edit `json`.

* __Why `jekyll` for static sites?__ `jekyll` provides predictable deployment on Github with `pages`.

* __Use `doctr` for integration__

* __`watchdog` for `development`__

        {% endraw %}
