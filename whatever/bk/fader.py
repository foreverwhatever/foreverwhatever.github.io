
# coding: utf-8

# In[101]:

import bokeh.plotting

from coffeetools import coffee
import jinja2, pandas

__all__ = ['sweet_fade']


# In[74]:

set_prop_state = """
window.scrolling ?= {{}}
window.scrolling[renderer.id] ?= {}
"""


# In[82]:

jssource = """
console.log renderer.id
dx = x.end - x.start
for prop, value of window.scrolling[renderer.id]
    t = dx/(value.lim[1]-value.lim[0])
    console.log t
    if 0 < t < 1
        updated = (1-t)*value.value[0] + t*value.value[1]
        if value['append']?
            updated += value.append
        renderer.glyph.set prop, updated
            
"""


# In[97]:

def sweet_fade(p, renderer, props):
    p.x_range.callback = bokeh.models.CustomJS(
        args={
            'x': p.x_range, 'y': p.y_range, 
            'renderer': renderer,
        },
        code=coffee.compile(
            '\n'.join([
                    set_prop_state.format(props.__str__()),
                    jssource
                ])
        )
    )

