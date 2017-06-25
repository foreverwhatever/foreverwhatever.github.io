from nbconvert.preprocessors import Preprocessor

class StripSource(Preprocessor):
    def preprocess_cell(self, cell, resources, index):
        if cell['cell_type'] == 'code':
            cell['source'] = """"""
        return cell, resources

c.TemplateExporter.template_file = '_layouts/jekyll.md.tpl'
c.TemplateExporter.filters = {
    'dump': 'json.dumps',
    'load': 'json.loads',
    'yaml': 'yaml.dump'
}
c.ExtractOutputPreprocessor.enabled = False
c.NbConvertBase.display_data_priority = [
    'text/html', 'text/markdown', 'image/svg+xml', 'text/latex', 'image/png',
    'image/jpeg', 'text/plain', 'application/javascript'
]

c.TemplateExporter.preprocessors = [
    'whatever.2017-06-24-Front-Matter-Preprocessor.FrontMatter', StripSource,
]
