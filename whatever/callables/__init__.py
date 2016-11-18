
# coding: utf-8

# In[1]:

from collections import OrderedDict
from toolz.curried import flip, juxt, map, partial, pipe, valmap
from types import LambdaType
from typing import Iterable, Any

__all__ = [
    'Dispatch', 'DictCallable', 'TupleCallable', 'ListCallable', 'SetCallable'
]


# In[2]:

class DictCallable(OrderedDict):
    def __call__(self, *args, **kwargs):
        return valmap(
            lambda x: 
            x(*args, **kwargs) 
            if callable(x) 
            else x, 
            self
        )


# In[24]:

class Condictional(OrderedDict):
    """First key to satisfy the key condition executes.
    """
    def _condition(self, function, *args, **kwargs)->bool:
        return function(*args, **kwargs)

    def __init__(self, *args, default=None, key=bool, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = default
        self.key = key

    def __call__(self, *args, **kwargs):
        for key, value in self.items():
            if self._condition(key, *args, **kwargs):
                if callable(value):
                    return value(*args, **kwargs)
                return value
        if self.default:
            return self.default(*args, **kwargs)
        raise KeyError(
            "No conditions satisfied for types: " + args.__str__())


# In[28]:

# Condictional({
#         lambda x: x>30: 20,
#         lambda x: x<100: lambda x: x *2,
#     })(31)


# In[14]:

class Dispatch(Condictional):
    """An object that provides multiple dispatch when it is called.
    """
    def _condition(self, types, *args, **kwargs)->bool:
        if not isinstance(types, Iterable):
            types = tuple([types])
        return pipe(
            zip(args, types),
            map(lambda arg: isinstance(*arg)),
            all
        )


# In[20]:

class SetCallable(set):
    def __call__(self, *args, **kwargs):
#         if pipe(self, map(
#                 partial(flip(isinstance), LambdaType)
#         ), any):
#             raise TypeError("Cannot interpolate a LambdaType.")
        values = map(lambda x: x(*args, **kwargs), self)
        return dict(zip(self, list(values)))


# In[22]:

# SetCallable({str.upper, len})('test')[str.upper]


# In[ ]:

class TupleCallable(tuple):
    def __call__(self, *args, **kwargs):
        return juxt(*self)(
            *args, **kwargs
        )


# In[5]:

class ListCallable(list):
    def __call__(self, *args, **kwargs):
        return list(juxt(*self)(
            *args, **kwargs
        ))

