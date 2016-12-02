
# coding: utf-8

# In[69]:

# import bokeh.plotting

from coffeetools import coffee
import bokeh, jinja2, pandas
from toolz.curried import *

__all__ = ['sweet_fade']


# In[59]:

# import bokeh.plotting

# import pandas

# bokeh.plotting.output_notebook()


# In[60]:

# "https://gist.github.com/tonyfast/a8f64cb2b8ce1c9eee32137ef15f8cb4"


# In[61]:

jssource = coffee.compile("""
window.record ?= 
    ct: 0
    fps: 100
    frames: []
        
if window.RECORD? and window.RECORD and window.record.ct % window.record.fps 
    el = "#modelid_"+p.get('id')+" canvas"
    window.record.frames.push jQuery(el)[0].toDataURL('image/png')
window.record.ct += 1""")


# In[62]:

def recorder(p):
    p.x_range.callback = bokeh.models.CustomJS(
        args={
            'x': p.x_range, 'y': p.y_range, 'p': p,
        },
        code=jssource,
    )


# In[68]:

recorder.__doc__ = """```javascript
// Change recording parameters with
window.RECORD = true
window.record // stores the data
Jupyter.notebook.kernel.execute("snapshots = " + JSON.stringify(window.record.frames))
```"""


# In[ ]:



