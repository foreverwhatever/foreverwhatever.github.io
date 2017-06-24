# coding: utf-8

# `foreverwhatever.github.io` is Tony Fast's personal journal of computational documents.

get_ipython().magic('load_ext literacy.template')
# ## The __build__ branch
# 
# The __build__ branch uses __travis-ci__ to transpile notebooks to a jekyll site on the __master__ 
# branch.  When __master__ updates, the standard github pages __jekyll__ build is used.
# 
# ### A collection of notebooks
# 
# Create a collection of ___notebooks__. It folder is the source of __markdown__, __json__, and
# __python__ copies of the collection.
# ### Python
# 
# The python __nbconvert__ configuration is *_layouts/python.py*.  The module is in a _non_-__Jekyll__ namespace;
# I personally chose __whatever__.

get_ipython().system(
    'jupyter nbconvert --config _layouts/python.py --output-dir=whatever _notebooks/*.ipynb'
)

# ### Markdown
# 
# The markdown __nbconvert__ configuration is *_layouts/markdown.py*
#         !jupyter nbconvert --config _layouts/markdown.py readme.ipynb
# 
# * Notebooks beginning with __Numbers__ are inferred as ___posts__

get_ipython().system(
    'jupyter nbconvert --config _layouts/markdown.py --output-dir _posts _notebooks/[0-9]*.ipynb'
)

# * Notebooks beginning with __Letters__ are inferred as ___docs__

get_ipython().system(
    'jupyter nbconvert --config _layouts/markdown.py --output-dir _docs _notebooks/[a-z,A-Z]*.ipynb'
)
# 
# ### Data
# 
# The data __nbconvert__ configuration is *_layouts/data.py*

get_ipython().system(
    'jupyter nbconvert --to notebook --config _layouts/data.py _notebooks/*.ipynb'
)
