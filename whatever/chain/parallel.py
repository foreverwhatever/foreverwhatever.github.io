
# coding: utf-8

# In[1]:

try:
    from .sugar import SugarChain
except:
    from sugar import SugarChain
import joblib
from toolz.curried import *


# In[58]:

@curry
def parallelize(func, args, n_jobs=4):
    """Parallelize an operation with joblib."""
    return joblib.Parallel(n_jobs=n_jobs)(
        joblib.delayed(func)(arg) for arg in args
    )


# In[60]:

class pchain(SugarChain):
    """A Parallelized chain."""
    def __init__(self, *args, **kwargs):
        n_jobs = 4
        if 'n_jobs' in kwargs: 
            n_jobs = kwargs['n_jobs']
            kwargs = dissoc(kwargs, 'n_jobs')
            
        self.n_jobs = n_jobs
        super(pchain, self).__init__(*args, **kwargs)
    
    def __mul__(self, value):
        return self[parallelize(value, n_jobs=self.n_jobs)]

