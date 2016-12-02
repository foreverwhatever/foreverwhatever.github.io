
# coding: utf-8

# In[1]:

import sklearn.datasets


# In[ ]:

def load(alias):
    data = getattr(sklearn.datasets, 'load_'+alias)()
    return data['data'], data['target'], data

