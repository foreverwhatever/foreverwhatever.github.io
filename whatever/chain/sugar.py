
# coding: utf-8

# In[1]:

try:
    from .chain import chain
except:
    from chain import chain

import collections
from toolz.curried import *


# In[57]:

class Sugar:
    def __add__(self, value):
        """Filter values
        chain(5).range + flip(operator.gt)(2)
        """
        return self.filter(value)

    def __gt__(self, value):
        """Execute a chain.
        chain(5).range > identity = range(5)
        """
        if value is compose:
            return self.compute
        return self[value].copy()
    
    def __mul__(self, value):
        """Map a function.
        chain(5).range + flip(operator.mul)(2)
        """
        return self.map(value)
    
    def __or__(self, value):
        """Pipe functions together.
        chain(5).range | list | len
        """
        return self[value]


# In[59]:

class SugarChain(chain, Sugar):
    def __getitem__(self, value):
        if isinstance(value, dict):
            return super(SugarChain, self).__getattr__(
                lambda x: valmap(lambda f: f(x) if callable(f) else f, value)
            )

        if not isinstance(value, str) and isinstance(value, collections.Iterable):
            return super(SugarChain, self).__getattr__(
                compose(type(value), juxt(*value))
            )
        
        return super(SugarChain, self).__getattr__(value)


# In[ ]:

class sweet(SugarChain):
    pass


# In[60]:

class _x(SugarChain):
    """Shorthand"""
    @property
    def _(self): return self.compute

class __x(SugarChain):
    """Shorthand"""
    @property
    def __(self): return self.compute

