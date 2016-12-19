
# coding: utf-8

# In[ ]:

try:
    from .chain import chain, Chain
    from .parallel import pchain
    from .sugar import _x, __x, sweet
except:
    from chain import chain, Chain
    from parallel import pchain
    from sugar import _x, __x, sweet

