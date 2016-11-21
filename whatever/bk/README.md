

```python
%reload_ext autoreload
%autoreload 2
```


```python
from whatever.bk.fader import sweet_fade
import bokeh.plotting

import pandas
```


```python
df = pandas.util.testing.makeDataFrame()
df['size']=20
```


```python
source = bokeh.models.ColumnDataSource(df)
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
p = bokeh.plotting.figure()
p.add_glyph(source, bokeh.models.Circle(x='A', y='B'))
text = p.add_glyph(source, bokeh.models.Text(x='A', y='B', text='size'))

sweet_fade(p, text, props)

bokeh.plotting.save(p)
pass
```


```python

```


```python

```
