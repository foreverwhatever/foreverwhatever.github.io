
# coding: utf-8

# Use `networkx` to compose function dependency graphs using function annotations.
# 
# * Parameters must be immutable during each computation.
# * Each computation should be pure.

# In[9]:

from itertools import zip_longest
from IPython import get_ipython
import networkx as nx
from toolz.curried import *

__all__ = ['build']


# In[10]:

_annotations_ = partial(flip(getattr), '__annotations__')
_name_ = lambda x: x if isinstance(x, str) else x.__name__


# In[11]:

def discover_annotated_functions(G, objs=get_ipython().user_ns):
    """Discover non-private annotated functions.
    """
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


# In[12]:

def nest_and_stringify(annotated):
    """Stringify function names in a graph like data structure.
    """
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


# In[13]:

def create_edges(G, nested_graph):
    """Add the graph edges based on the annotations.
    """
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


# In[1]:

def find_longest_path(start, end, G):
    """Find the longest path of functions.
    """
    return list(nx.all_simple_paths(G, start.__name__, end.__name__))


# In[7]:

def run(G, paths, **kwargs):
    """Iterate through the path and execute the function.
    """
    G.add_nodes_from(kwargs)
    nx.set_node_attributes(G, 'value', None)
    nx.set_node_attributes(G, 'value', kwargs)
    for path in paths:
        for function in path:
            if G.node[function]['value'] is None:
                params = pipe(
                    G.node[function]['func'],
                    _annotations_,
                    valmap(_name_),
                    valmap(G.node.__getitem__),
                    valmap(get('value'))
                )
                if not any(map(lambda x: x is None, params.values())):
                    nx.set_node_attributes(
                        G, 'value', {
                            function: G.node[function]['func'](**params)
                        }
                    )
    return G


# In[8]:

def build(start, end, objs=get_ipython().user_ns, G=nx.Graph()):
    """Build a higher order function from the
    objects in `objs` that begins start and terminates at end.  The
    resulting function computes all nodes along the longest path
    storing the values in the networkx graph..
    """
    path = pipe(
        discover_annotated_functions(G, objs),
        nest_and_stringify,
        partial(create_edges, G),
        partial(find_longest_path, start, end)
    )
    return partial(run, G, path)


# In[ ]:



