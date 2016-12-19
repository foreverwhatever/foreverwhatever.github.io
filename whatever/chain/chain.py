
# coding: utf-8

# In[1]:

import collections
from future import builtins
from toolz.curried import *
import toolz.curried
from toolz.functoolz import Compose

__all__ = ['Chain', 'chain']


# In[1]:

class Namespace(object):
    imports = (
        toolz.curried,
        operator,
        builtins,
    )
    
    @property
    def namespace(self):
        return pipe(
            self.imports,
            reversed,
            map(
                lambda x: 
                x if isinstance(x, dict) 
                else vars(x)
            ), 
            lambda x: merge(*x),
            keyfilter(compose(str.islower, first))
        )


# In[37]:

class Chain(Namespace):    
    
    def __init__(self, *args, **kwargs):
        self.tokens = list()
        self.args = args
        self.kwargs = kwargs
        
    def __getattr__(self, attr):        
        if isinstance(attr, str):
            try:
                attr = super(Chain, self).namespace[attr]
            except AttributeError:
                raise AttributeError(attr)
            
        
        if callable(attr) or first(attr) is not '_':
            self.tokens.append(
                [attr, tuple(), dict(),]
            )
        
        return self
    
    @staticmethod
    def _token_to_function(token):
        func, args, kwargs = token
        if args or kwargs:
            return partial(func, *args, **kwargs)
        return func
        
    @property
    def funcs(self):
        return pipe(
            self.tokens, 
            map(self._token_to_function),
            tuple,
        )
       
    def __call__(self, *args, **kwargs):
        self.tokens[-1][1:] = args, kwargs
        return self
    
    def __dir__(self):
        return dict.keys(self.namespace)

    def compute(self, *args, **kwargs):
        if not(args or kwargs):
            args = self.args
            kwargs = self.kwargs
        return self.compose(*args, **kwargs)
    
    def copy(self):
        value = self.__class__(*self.args, **self.kwargs)
        value.tokens = self.tokens.copy()
        return value
    
    @property
    def compose(self):
        return pipe(
            self.funcs,
            tuple,
            reversed,
            lambda x: compose(*x),
        )
            
Chain.__getitem__ = Chain.__getattr__


# In[56]:

class chain(Chain):
    """Add a repr method that computes the value
    based on the chain args and kwargs.  They can 
    be overridden in the compute attribute."""
    def __repr__(self):
        value = None
        try:
            value = self.compute()
        except: pass
        
        if value is not None:
            try:
                return str(value)
            except: pass
        
        return self.compose.__repr__()

