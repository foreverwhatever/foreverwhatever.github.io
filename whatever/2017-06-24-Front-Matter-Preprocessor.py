# coding: utf-8

# # Front Matter `nbconvert` preprocessor
#
# Append *metadata* and *resources* as front matter to a notebook; insert a markdown cell at the beginning of notebook.

o = __name__ == '__main__'
if o:
    get_ipython().magic('reload_ext literacy.template')


def safe(object):
    """Make sure all Mapping objects are pure python __dict__s
    
    """
    if hasattr(object, 'items'):
        object = dict(object)
        for key, value in object.items():
            object.update({key: safe(value)})
    return object


class FrontMatter(__import__('nbconvert').preprocessors.Preprocessor):
    def preprocess(self, nb, resources={}):
        source = __import__('yaml').safe_dump(
            safe({**resources, **nb['metadata']}), default_flow_style=False)
        nb['cells'].insert(0,
                           __import__('nbformat').v4.new_markdown_cell(
                               """---\n{}\n---\n""".format(source)))
        return nb, resources


exporter = __import__('nbconvert').get_exporter('markdown')(config={
    'TemplateExporter': {
        'preprocessors': ['literacy.preprocessors.Dedent', FrontMatter]
    }
})
# ---
#
# > The snippet below shows the composed code.
#
# <pre><code>{{o and exporter.from_filename('2017-06-24-Front-Matter-Preprocessor.ipynb')[0].lstrip()}}</code></pre># __normalize__ all the values of a collection to a basic `dict` type for `yaml.safe_load` to consume.
