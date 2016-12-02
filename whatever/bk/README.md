

```python
%reload_ext autoreload
%autoreload 2
```


```python


from whatever.bk import DataSource, Join
from whatever.bk.fader import sweet_fade
import pandas
```


```python
from whatever.nxecute import Compositions
from whatever.nxecute.recipes import SciKit
from sklearn import datasets, discriminant_analysis
G = Compositions(vars(SciKit))
DATA = G.Compose('load')().node['load']['return']
H = G.Compose('fit')(X=DATA[0], y=DATA[1], MODEL=discriminant_analysis.LinearDiscriminantAnalysis())
```


```python
df = pandas.DataFrame(H.node['transform']['return'], H.node['predict']['return'])
```


```python
import bokeh.plotting
```


```python
xx = list(df.describe().loc['std'][0]*pandas.np.array([.1, 10]))
```


```python
props = {
    'fill_alpha': {
        'lim': xx,
        'value': [.9, .1],
    },
}
```


```python
with DataSource(df, x=0, y=1) as source:
    p = bokeh.plotting.figure(responsive=True, webgl=True)
    Glyph = Join(p, source)
    overlay = Glyph(bokeh.models.Circle, size=40, line_alpha=0)
    sweet_fade(p, overlay, props)
    bokeh.plotting.save(p)
```


```python
from whatever.bk.fader import sweet_fade
from whatever.bk import DataSource, Figure, Join

import bokeh.plotting

import pandas
```


```python
df = pandas.util.testing.makeDataFrame()
df['size']=20
```


```python
props = {
    'text_alpha': {
        'lim': [.001, 20],
        'value': [.9, .1],
    },
    'text_font_size': {
        'lim': [.001, 20],
        'value': [40, 10],
        'append': 'pt',
    }
}
```


```python
props = {
    'text_alpha': {
        'lim': [.001, 20],
        'value': [.9, .1],
    },
    'text_font_size': {
        'lim': [.001, 20],
        'value': [40, 10],
        'append': 'pt',
    }
}
```


```python
with \
DataSource(df, x='A', y='B', text='size') as source, \
Figure() as p:    
    
    Glyph = Join(p, source)
    
    Glyph(bokeh.models.Circle, size='text')
    
    sweet_fade(p, Glyph(bokeh.models.Text), props)
    
    bokeh.plotting.show(p);
```

    WARNING://anaconda/lib/python3.5/site-packages/bokeh/core/validation/check.py:W-1000 (MISSING_RENDERERS): Plot has no renderers: Figure, ViewModel:Plot, ref _id: e210e8be-0d0d-4344-a5b6-6ff0e0daa8a3



```python

from sklearn import datasets

G = Compositions(vars(SciKit)).Compose('load')

G(ALIAS='iris')
```


```python
iris = datasets
```


```python

```


```python
with \
DataSource(df, x='A', y='B', text='size') as source, \
Figure() as p:    
    
    Glyph = Join(p, source)
    
    Glyph(bokeh.models.Circle, size='text')
    
    sweet_fade(p, Glyph(bokeh.models.Text), props)
    
    bokeh.plotting.show(p);
```
