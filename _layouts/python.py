c.NbConvertApp.export_format = 'python'
c.TemplateExporter.filters = {
    'dump': 'json.dumps',
    'load': 'json.loads',
    'yaml': 'yaml.dump'
}

c.TemplateExporter.template_file = '_layouts/docify.tpl'

c.TemplateExporter.preprocessors = [
    'literacy.preprocessors.NumberCell', 'literacy.preprocessors.Explode',
    'literacy.preprocessors.Dedent'
]
