
# Adding `post_save` behavior to `JupyterApp`

> Look into your `.jupyter` directory.


```python
%ls ~/.jupyter/
```

> If `jupyter_notebook_config.py` does/doesn't exist then execute the cell below to add a `post_save` hook.

__The Hook__ - Each time you save a notebook with `_nbconvert.py` in its directory.  The code will be convert to reusable python.


```python
%%file ~/.jupyter/jupyter_notebook_config.py --append
# %load __init__.py
import importlib, inspect, os
from subprocess import check_call

c = get_config()

def post_save(model, os_path, contents_manager):
    """post-save hook for converting notebooks using local config files."""

    # Only convert notebooks
    if model['type'] != 'notebook': return

    directory, fname = os.path.split(os_path)
    
    if os.path.isfile(os.path.join(directory, '_nbconvert.py')):
        # Common to each call
        call = ['jupyter','nbconvert', '--to']

        # Export README's as markdown to their local directory.
        if fname == 'README.ipynb':
            call_md = call.copy()
            call_md.extend(['markdown', fname])
            check_call(call_md, cwd=directory)
        
        # Run nbconvert with specific config options.
        elif not ' ' in fname:
            call.extend(['script', '--config', '_nbconvert.py', fname])
            check_call(call, cwd=directory)


c.FileContentsManager.post_save_hook = post_save
```
