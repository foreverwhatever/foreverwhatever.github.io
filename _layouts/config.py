c.TemplateExporter.filters = {
    'dump': 'json.dumps',
    'load': 'json.loads',
    'yaml': 'yaml.dump'
}

c.TemplateExporter.preprocessors = [
    'literacy.preprocessors.Explode', 'literacy.preprocessors.Dedent'
]
