
# Violent Abuse of Annotations

Consider the functions below.  The annotations define the functions that are required to complete before the others can execute.  `strings` are set as variables later.


```python
%reload_ext autoreload
%autoreload 2
```


```python
def f(a:'A'):
    return a

def g(a:f, b:'B'):
    return a+b

def h(a:f, b:g):
    return a*b
```


```python
from whatever.consumer import consume
```


```python
consume(f, h, A=10, B=32).node
```




    {'A': {'value': 10},
     'B': {'value': 32},
     'f': {'func': <function __main__.f>, 'value': 10},
     'fit': {'func': <function __main__.fit>},
     'g': {'func': <function __main__.g>, 'value': 42},
     'h': {'func': <function __main__.h>, 'value': 420},
     'load': {'func': <function __main__.load>},
     'model': {'func': <function __main__.model>},
     'transform_and_predict': {'func': <function __main__.transform_and_predict>}}




```python
import sklearn.datasets, sklearn.discriminant_analysis
from whatever.harness import Harness
```


```python
def load(alias:'ALIAS'):
    data = getattr(sklearn.datasets, 'load_'+alias)()
    return Harness(
        data=data['data'],
        index=data['target'],
    )
```


```python
def model(df:load):
    return df.set_params(
        estimator=sklearn.discriminant_analysis.LinearDiscriminantAnalysis(),
        feature_level=-1,
    )
```


```python
def fit(df:model, samples:'SAMPLES'):
    df.sample(samples).fit()
    return df
```


```python
def transform_and_predict(df:fit):
    return df.transform().set_index(df.predict()[0], append=True)
```


```python
consume(
    load, transform_and_predict, 
    ALIAS='iris', SAMPLES=100,
).node[transform_and_predict.__name__]['value']
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
      <th rowspan="30" valign="top">0</th>
      <th>0</th>
      <td>8.310175</td>
      <td>0.403879</td>
    </tr>
    <tr>
      <th>0</th>
      <td>7.315481</td>
      <td>-0.698621</td>
    </tr>
    <tr>
      <th>0</th>
      <td>7.781817</td>
      <td>-0.092793</td>
    </tr>
    <tr>
      <th>0</th>
      <td>7.064578</td>
      <td>-0.456312</td>
    </tr>
    <tr>
      <th>0</th>
      <td>8.422995</td>
      <td>0.666523</td>
    </tr>
    <tr>
      <th>0</th>
      <td>7.897895</td>
      <td>1.580563</td>
    </tr>
    <tr>
      <th>0</th>
      <td>7.542241</td>
      <td>0.611076</td>
    </tr>
    <tr>
      <th>0</th>
      <td>7.833632</td>
      <td>0.120901</td>
    </tr>
    <tr>
      <th>0</th>
      <td>6.833580</td>
      <td>-0.780648</td>
    </tr>
    <tr>
      <th>0</th>
      <td>7.535152</td>
      <td>-0.835844</td>
    </tr>
    <tr>
      <th>0</th>
      <td>8.602686</td>
      <td>0.698113</td>
    </tr>
    <tr>
      <th>0</th>
      <td>7.469910</td>
      <td>0.100566</td>
    </tr>
    <tr>
      <th>0</th>
      <td>7.540001</td>
      <td>-0.957743</td>
    </tr>
    <tr>
      <th>0</th>
      <td>7.954521</td>
      <td>-0.565608</td>
    </tr>
    <tr>
      <th>0</th>
      <td>10.093828</td>
      <td>1.516946</td>
    </tr>
    <tr>
      <th>0</th>
      <td>9.435495</td>
      <td>2.814042</td>
    </tr>
    <tr>
      <th>0</th>
      <td>8.860678</td>
      <td>1.902724</td>
    </tr>
    <tr>
      <th>0</th>
      <td>8.024142</td>
      <td>0.693104</td>
    </tr>
    <tr>
      <th>0</th>
      <td>8.194135</td>
      <td>0.968490</td>
    </tr>
    <tr>
      <th>0</th>
      <td>8.306447</td>
      <td>1.310187</td>
    </tr>
    <tr>
      <th>0</th>
      <td>7.598294</td>
      <td>-0.160591</td>
    </tr>
    <tr>
      <th>0</th>
      <td>7.846080</td>
      <td>1.366870</td>
    </tr>
    <tr>
      <th>0</th>
      <td>9.139725</td>
      <td>1.109095</td>
    </tr>
    <tr>
      <th>0</th>
      <td>6.381321</td>
      <td>0.564849</td>
    </tr>
    <tr>
      <th>0</th>
      <td>6.747823</td>
      <td>-0.141055</td>
    </tr>
    <tr>
      <th>0</th>
      <td>6.895602</td>
      <td>-0.889804</td>
    </tr>
    <tr>
      <th>0</th>
      <td>7.020870</td>
      <td>0.618809</td>
    </tr>
    <tr>
      <th>0</th>
      <td>8.130993</td>
      <td>0.293236</td>
    </tr>
    <tr>
      <th>0</th>
      <td>8.197355</td>
      <td>0.141235</td>
    </tr>
    <tr>
      <th>0</th>
      <td>7.059729</td>
      <td>-0.334414</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="13" valign="top">2</th>
      <th>2</th>
      <td>-7.462203</td>
      <td>1.774883</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-6.175545</td>
      <td>1.012703</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-9.216288</td>
      <td>-1.069180</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-5.347218</td>
      <td>-0.009006</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-6.838830</td>
      <td>1.489181</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-6.569584</td>
      <td>-0.003168</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-4.993702</td>
      <td>0.334179</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-4.947244</td>
      <td>0.748823</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-7.654342</td>
      <td>0.497323</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-5.864793</td>
      <td>-0.885618</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-7.670620</td>
      <td>-0.784854</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-6.627839</td>
      <td>1.437647</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-7.940375</td>
      <td>0.786548</td>
    </tr>
    <tr>
      <th>1</th>
      <th>1</th>
      <td>-4.796176</td>
      <td>-0.805218</td>
    </tr>
    <tr>
      <th rowspan="16" valign="top">2</th>
      <th>2</th>
      <td>-6.185316</td>
      <td>-1.902020</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-8.281547</td>
      <td>0.746817</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-7.527954</td>
      <td>2.790346</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-6.032545</td>
      <td>0.407815</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-4.768062</td>
      <td>0.859466</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-6.342383</td>
      <td>1.205514</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-7.804901</td>
      <td>1.972311</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-6.192362</td>
      <td>2.025583</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-6.422210</td>
      <td>0.269652</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-8.005108</td>
      <td>1.643905</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-7.982963</td>
      <td>2.646078</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-6.730418</td>
      <td>1.772707</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-6.222615</td>
      <td>-0.265404</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-5.995345</td>
      <td>0.965240</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-6.822042</td>
      <td>2.692305</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-5.551663</td>
      <td>0.647948</td>
    </tr>
  </tbody>
</table>
<p>150 rows × 2 columns</p>
</div>




```python

```
