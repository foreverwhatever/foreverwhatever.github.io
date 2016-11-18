
# `nbrerun`

Create derived notebooks an existing notebook by replacing string tokens and executing the notebook.

## Usage

* Requires a running notebook.
* Create a `yaml` or `json` file with `files` and `globals` keys
* Run the `luigi` command line task 



```python
%%file replacements.yaml
globals: {}
files:
    'digits.ipynb':
        '_iris': '_digits'
    'diabetes.ipynb':
        '_iris': '_diabetes'        
```


```python
!rm -rf demo
!mkdir demo
!luigi \
--module whatever.nbrerun BulkReplaceAndExecute \
--notebook parent.ipynb \
--execute \
--output-dir demo \
--workers 2 \
--local-scheduler  
```
