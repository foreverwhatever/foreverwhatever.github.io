c.TemplateExporter.template_file = '_layouts/jekyll.md.tpl'
c.TemplateExporter.filters = {
    'dump': 'json.dumps',
    'load': 'json.loads',
    'yaml': 'yaml.dump'
}
c.ExtractOutputPreprocessor.enabled = False

c.TemplateExporter.preprocessors = [
    'literacy.preprocessors.JoinSource',
    'whatever.2017-06-24-Front-Matter-Preprocessor.FrontMatter',
]
