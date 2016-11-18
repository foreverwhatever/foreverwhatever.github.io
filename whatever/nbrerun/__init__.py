
# coding: utf-8

# # Using `luigi` to Autogenerate Executed Notebooks

# In[11]:

import luigi
from luigi.util import inherits, requires
from toolz.curried import merge
import nbconvert, nbformat, os, yaml


# In[5]:

class TheReplacements(luigi.ExternalTask):
    """Load a replacement file.
    """
    replacements = luigi.Parameter('replacements.yaml')
    
    def output(self):
        return luigi.LocalTarget(self.replacements)


# In[6]:

class TheNotebook(luigi.ExternalTask):
    """Load a notebook
    """
    notebook = luigi.Parameter()
    
    def output(self):
        return luigi.LocalTarget(self.notebook)


# In[7]:

@requires(TheNotebook)
class DerivedNotebook(luigi.Task):
    """Make a copy of a notebook"""
    target_name = luigi.Parameter()
    
    def run(self):
        with self.input().open('r') as inp:
            nb = nbformat.read(inp, 4)
        with self.output().open('w') as out:
            nbformat.write(nb, out)
    
    def output(self):
        return luigi.LocalTarget(self.target_name)


# In[8]:

@requires(DerivedNotebook)
class ReplaceAndExecute(luigi.Task):
    """Replace a notebook using specific keys are execute it.
    """
    replacement = luigi.DictParameter()

    def run(self):
        with self.input().open('r') as f:
            nb = nbformat.read(f, 4)
            
        for cell in nb['cells']:
            for token, replacement in self.replacement.items():
                cell['source'] = cell['source'].replace(
                    token, replacement
                )
            if 'outputs' in cell:
                cell['outputs'] = []
                
        with self.output().open('w') as f:
            nbformat.write(nb, f)
    
    def output(self):
        return luigi.LocalTarget(self.target_name)            


# In[9]:

@requires(ReplaceAndExecute)
class Executor(luigi.Task):
    """Logic to execute a notebook during the task
    """
    execute = luigi.BoolParameter()
    def run(self):
        if self.execute:
            with self.input().open('r') as inp:
                nb = nbformat.read(inp, 4)
            ep = nbconvert.preprocessors.ExecutePreprocessor()
            ep.preprocess(nb, {})
            with self.output().open('w') as out:
                nbformat.write(nb, out)
    
    def output(self):
        return luigi.LocalTarget(self.target_name)            


# In[10]:

@inherits(TheNotebook)
class BulkReplaceAndExecute(luigi.Task):
    execute = luigi.BoolParameter()
    output_dir = luigi.Parameter('.')
    replacements = luigi.Parameter('replacements.yaml')
    
    def requires(self):
        return TheReplacements(self.replacements)
    
    def run(self):
        with self.input().open('r') as f:
            replacements = yaml.safe_load(f)
        
        for target_name, replacement in replacements['files'].items():
            
            yield self.clone(
                Executor,
                notebook=self.notebook, 
                replacement=merge(
                    self.replacements['globals']
                    if 'globals' in self.replacements
                    else {}
                    , replacement
                ),
                target_name=os.path.join(self.output_dir, target_name),
                execute=self.execute,
            )

