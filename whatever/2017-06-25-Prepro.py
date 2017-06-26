# coding: utf-8


# This notebook makes it easier to create preprocessors for __nbconvert__.  These should work on an existing exporter.

get_ipython().magic('load_ext literacy.template')

from nbconvert import export, get_exporter

class SomeNewPreProcessor(Preprocessor): 
    def preprocess(self, nb, resources={}):
        return nb, resources

    def preprocess_cell(self, nb, resources, index):
        return nb, resources

class my_decorator(object):
    """[# PythonDecorators/my_decorator.py](http://python-3-patterns-idioms-
    test.readthedocs.io/en/latest/PythonDecorators.html#function-decorators)
    """

    def __init__(self, f):
        print("inside my_decorator.__init__()")
        f() # Prove that function definition has completed

    def __call__(self):
        print("inside my_decorator.__call__()")

@my_decorator
def aFunction():
    print("inside aFunction()")

print("Finished decorating aFunction()")

aFunction()
# * There is a decorator that does that following
# 
#  * Let's make a simple cell preprocessor that appends the cell index to the cell metadata.
# 
#  * Let's make a simple notebook preprocessor that capitalizes markdown cells.
# * There is a decorator that does that following
# 
#  * Let's make a simple cell preprocessor that appends the cell index to the cell metadata.
# 
#  * Let's make a simple notebook preprocessor that capitalizes markdown cells.

exporter = get_exporter('markdown')(config={
    'TemplateExporter': {
        'preprocessors': []
    }
})

print(exporter.from_filename('Untitled55.ipynb')[0])
# ---