
# coding: utf-8

# In[2]:

from itertools import zip_longest
from IPython import get_ipython
import networkx as nx
from toolz.curried import *


# In[3]:

_annotations_ = partial(flip(getattr), '__annotations__')
_name_ = lambda x: x if isinstance(x, str) else x.__name__


# In[9]:

def discover_annotated_functions(G, objs=get_ipython().user_ns):
    return pipe(
        objs,
        keyfilter(lambda x: x[0] != '_'),
        valfilter(
            excepts(
                AttributeError,
                _annotations_,
                lambda x: False
            )
        ), 
        do(G.add_nodes_from),
        do(
            partial(nx.set_node_attributes, G, 'func')
        )
    )


# In[10]:

def nest_and_stringify(annotated):
    return pipe(
        annotated, 
        
        valmap(
            _annotations_
        ), 
        valmap(
            valfilter(callable)
        ),
        valmap(
            valmap(_name_)
        ),
    )


# In[11]:

def create_edges(G, nested_graph):
    edges = pipe(
        nested_graph.items(),
        map(
            lambda x: 
            zip_longest((first(x),), second(x).values(), fillvalue=first(x)),
        ),
        concat,
        tuple,
    )
    G.add_edges_from(edges)
    return G


# In[12]:

def find_longest_path(start, end, G):
    return pipe(
        nx.all_simple_paths(G, start.__name__, end.__name__),
        topk(1, key=len),
        first,
        map(compose(get('func'), G.node.__getitem__)),
#         filter(lambda x: hasattr(x, 'func')),
        list
    )


# In[21]:

def run(G, path):
    for function in path:
        params = pipe(
            function,
            _annotations_,
            valmap(_name_),
            valmap(G.node.__getitem__),
            valmap(get('value'))
        )
        nx.set_node_attributes(
            G, 'value', {
                function.__name__: function(**params)
            }
        )
    return G


# In[20]:

def consume(start, end, objs=get_ipython().user_ns, **kwargs):
    G = nx.Graph()
    G.add_nodes_from(kwargs)
    nx.set_node_attributes(
        G, 'value', kwargs
    )
    path = pipe(
        discover_annotated_functions(G, objs),
        nest_and_stringify,
        partial(create_edges, G),
        partial(find_longest_path, start, end)
    )
    return run(G, path)

