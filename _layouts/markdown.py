c.ExtractOutputPreprocessor.enabled=False
c.TemplateExporter.filters = {
    'dump': 'json.dumps',
    'load': 'json.loads',
    'yaml': 'yaml.dump'
}
c.NbConvertBase.display_data_priority = ['text/html', 'text/markdown', 'image/svg+xml', 'text/latex', 'image/png', 'image/jpeg', 'text/plain', 'application/javascript']