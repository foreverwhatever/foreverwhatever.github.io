
# coding: utf-8

# In[1]:

import bokeh.plotting

# from coffeetools import coffee
import jinja2, pandas
from toolz.curried import *

__all__ = ['sweet_fade']


# In[2]:

# set_prop_state = coffee.compile("""
# window.scrolling ?= {}
# window.scrolling[renderer.id] ?= {}
# """, bare=True)


# In[4]:

# with open('templates/fader/globals.js.tpl', 'w') as f:
#     pipe(
#         interleave([set_prop_state.split('{}'), ['{}', '{{props}}']]),
#         list, 
#         ''.join,
#         f.write
#     )


# In[5]:

# jssource = """
# window.fader_callback ?= (x, y, renderer)->
#     dx = x.end - x.start
#     for prop, value of window.scrolling[renderer.id]
#         t = dx/(value.lim[1]-value.lim[0])
#         console.log t
#         if 0 < t < 1
#             updated = (1-t)*value.value[0] + t*value.value[1]
#             if value['append']?
#                 updated += value.append
#             renderer.glyph.set prop, updated"""


# In[6]:

# with open('templates/fader/fader_callback.js', 'w') as f:
#     pipe(
#         coffee.compile(jssource, bare=True), 
#         f.write
#     )


# In[7]:

env = jinja2.Environment(loader=jinja2.PackageLoader('whatever.bk', 'templates/fader'))


# In[10]:

call_it = """
fader_callback(x, y, renderer);
"""


# In[11]:

def sweet_fade(p, renderer, props):
    p.x_range.callback = bokeh.models.CustomJS(
        args={
            'x': p.x_range, 'y': p.y_range, 
            'renderer': renderer,
        },
        code='\n'.join([
                env.get_template('globals.js.tpl').render(props=props),
                env.get_template('fader_callback.js').render(),
                call_it,
            ])
    )

