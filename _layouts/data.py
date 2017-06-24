c.Exporter.file_extension = '.json'
c.FilesWriter.build_directory = '_data'
c.ClearOutputPreprocessor.enabled = True
c.Exporter.preprocessors = [
    'literacy.preprocessors.Explode', 'literacy.preprocessors.Dedent'
]
