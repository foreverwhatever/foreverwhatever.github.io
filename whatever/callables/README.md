

```python
import whatever.callables
```


```python
whatever.callables.__all__
```




    ['Dispatch', 'DictCallable', 'TupleCallable', 'ListCallable', 'SetCallable']



# `callables`

What if python objects were callable?

|Object| Action|
|---|---|
|Dispatch|Multiple Dispatch Dictionary|
|DictCallable|Callable Dictionary|
|TupleCallable|Callable Tuple|
|ListCallable|Callable List|
|SetCallable|Callable Set that transform to a dictionary|

## `dispatch`


```python
dispatcher = whatever.callables.Dispatch((
    (str, str.upper),
    ((int, float), lambda x: x*10)
))
```


```python
print(dispatcher('dispatch 🚬'), dispatcher(42))
```

    DISPATCH 🚬 420


# `SetCallable`

Transforms a set of functions into a dictionary, the keys correspond to a function.

This is influenced by `coffee☕️script` object interpolation .


```python
reverse = lambda x: x[::-1]
result = whatever.callables.SetCallable({
        str.upper, len, reverse
    })('test')
```


```python
result[reverse]
```




    'tset'


