
# Violent Abuse of Annotations

Consider the functions below.  The annotations define the functions that are required to complete before the others can execute.  `strings` are set as variables later.


```python
%reload_ext autoreload
%autoreload 2
```


```python
def f(a: 'A'):
    return a

def g(a: f, b: 'B'):
    return a+b

def h(a: f, b: g):
    return a*b
```


```python
from whatever.consumer import consume
```


```python
F = consume(f, h)
F(A=10, B=32).node
```




    {'A': {'value': 10},
     'B': {'value': 32},
     'f': {'func': <function __main__.f>, 'value': 10},
     'g': {'func': <function __main__.g>, 'value': 42},
     'h': {'func': <function __main__.h>, 'value': 420}}




```python
import sklearn.datasets, sklearn.discriminant_analysis
from whatever.harness import Harness
```


```python
def load(alias: 'ALIAS'):
    data = getattr(sklearn.datasets, 'load_'+alias)()
    return Harness(
        data=data['data'],
        index=data['target'],
    )
```


```python
def model(df: load):
    return df.set_params(
        estimator=sklearn.discriminant_analysis.LinearDiscriminantAnalysis(),
        feature_level=-1,
    )
```


```python
def fit(df: model, samples: 'SAMPLES'):
    df.sample(samples).fit()
    return df
```


```python
def transform_and_predict(df: fit):
    return df.transform().set_index(df.predict()[0], append=True)
```


```python
G = consume(load, transform_and_predict)
graph = G(ALIAS='iris', SAMPLES=100)
```


```python
graph.node[transform_and_predict.__name__]['value'].sample(2)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th></th>
      <th>0</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <th>1</th>
      <td>-1.043577</td>
      <td>-2.472912</td>
    </tr>
    <tr>
      <th>2</th>
      <th>2</th>
      <td>-6.604323</td>
      <td>0.534927</td>
    </tr>
  </tbody>
</table>
</div>


