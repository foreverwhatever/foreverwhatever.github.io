c.TemplateExporter.template_file = '_layouts/jekyll.md.tpl'
c.TemplateExporter.filters = {
    'dump': 'json.dumps',
    'load': 'json.loads',
    'yaml': 'yaml.dump'
}
c.ExtractOutputPreprocessor.enabled = False
c.NbConvertBase.display_data_priority = [
    'application/javascript', 'text/html', 'text/markdown', 'image/svg+xml', 'text/latex', 'image/png',
    'image/jpeg', 'text/plain'
]

c.TemplateExporter.preprocessors = [
    'whatever.2017-06-24-Front-Matter-Preprocessor.FrontMatter',
    'literacy.preprocessors.JoinSource',
]
