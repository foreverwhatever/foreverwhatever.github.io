
# coding: utf-8

# In[6]:

import bokeh.models
import bokeh.plotting
import contextlib
from toolz.curried import *


# In[7]:

@contextlib.contextmanager
def DataSource(df, **kwargs):
    """Minimize errant bokeh data sources.
    """
    source = (
        df
        .rename(
            columns=merge(
                pipe(df.columns, map(juxt(identity, str)), dict),
                pipe(kwargs, itemmap(reversed)),
            )
        )
        .pipe(bokeh.models.ColumnDataSource)
    )
    yield source
    del source


# In[8]:

@contextlib.contextmanager
def Figure(**kwargs):
    p = bokeh.plotting.figure(**kwargs)
    yield p
    while p.renderers:
        renderer = p.renderers.pop()
        del renderer
    del p


# In[9]:

@curry
def Join(p, source, model, **kwargs):
    """Join a data source and a model.
    """
    return pipe(
        source.column_names, 
        filter(operator.contains(model.properties())),
        map(juxt(identity, identity)),
        dict,
        lambda x: merge(x, kwargs),
        lambda x: p.add_glyph(source, model(**x))
    )


# In[ ]:



