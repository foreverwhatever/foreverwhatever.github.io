c.NbConvertApp.export_format = 'markdown'
c.FilesWriter.build_directory = '_posts'
c.TemplateExporter.template_file = '_layouts/jekyll.md.tpl'
c.TemplateExporter.filters = {
    'dump': 'json.dumps',
    'load': 'json.loads',
    'yaml': 'yaml.dump'};c.ExtractOutputPreprocessor.enabled=False;
c.NbConvertBase.display_data_priority = ['text/html', 'text/markdown', 'image/svg+xml', 'text/latex', 'image/png', 'image/jpeg', 'text/plain', 'application/javascript']