# coding: utf-8

# # <del>`fidget`</del> <small>a `pythonic` functional programming `object`</small>
#
# > ...posers juxtapose juxtapositions
#
# > composers compose compositions

from fidget import pipes as a, maps
an = the = then = a
from copy import copy
import pandas, requests, toolz

triangles = a.combinations(r=2).zip(list('ABC'))[maps.concat().list()].concatv(
    [list('ABC')]).list()('DEF')
triangles

positions = {
    'A': [-1, 0],
    'B': [0, 1],
    'C': [1, 0],
    'D': [-.5, .5],
    'E': [0, 0],
    'F': [.5, .5],
}
