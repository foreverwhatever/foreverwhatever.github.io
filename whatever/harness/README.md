
# `tidy-harness`

A _tidy_ `pandas.DataFrame` with `scikit-learn` models, interactive `bokeh` visualizations, and `jinja2` templates.

## Usage

### Example: Modeling Fisher's 🌸 Data


```python
import tonyfast.harness
```


```python
from tonyfast.harness import Harness
from pandas import Categorical
from sklearn import datasets, discriminant_analysis
iris = datasets.load_iris()

# Harness is just a dataframe
df = Harness(
    data=iris['data'], index=Categorical(iris['target']),
    estimator=discriminant_analysis.LinearDiscriminantAnalysis(),
    feature_level=-1, # the feature level indicates an index 
                      # in the dataframe. -1 is the last index.
)

# Fit the model with 50 random rows.
df.sample(50).fit()

# Transform the dataframe
transformed = df.transform()
transformed.set_index(
    df.index
    .rename_categories(iris['target_names'])
    .rename('species'), append=True, inplace=True,
)

# Plot the dataframe using Bokeh charts.
with transformed.reset_index().DataSource(x=0, y=1) as source:
    source.Scatter(color='species')
    source.show()
```

### More Examples

More examples can be found in the [`tests`](https://github.com/tonyfast/tidy-harness/tree/master/tests) directory.  Tap the __Ⓣ key__ while in the Github interface to search quickly.

## Background

`harness` initially responded to the need for `scikit-learn` models closer to a `pandas.DataFrame`.  Since a DataFrame is __[Tidy Data](http://vita.had.co.nz/papers/tidy-data.pdf)__ the rows and columns can assist in tracking samples and features over many estimations.  With this knowledge it would be easier to design a testing harness for data science.

The `DataFrame` has a powerful declarative syntax, consider the `groupby` and `rolling` apis.  There is a modern tendency toward declarative and functional syntaxes in scientific computing and visualization.  This is observed in [altair](https://github.com/altair-viz/altair), dask, and scikit-learn.

`tidy-harness` aims to provide a chain interface between `pandas.DataFrame` objects and other popular scientific computing libraries in the python ecosystem.  The initial `harness` extensions :

* attach a `scikit-learn` estimator to the dataframe.
* attach a shared `jinja2` environment to render narratives about the dataframes.
* `bokeh` plotting methods with a `contextmanager` for interactive visualization development

## Development

> The development scripts can be run through this notebook.

Jupyter notebooks are used for all Python development in this project.  The key features are:

* [`watchdog`]() file system watcher that converts notebooks to python scripts with `nbconvert`.  _Tests are not converted._
* [`nbconvert`]() with the `--execute` flag to run notebooks and fill out their output.  _The current goal is for the notebook to be viewable in a Github repo.
* [`pytest-ipynb`]() to run tests directly on the notebooks.

### Making the python module

The script below:

* Installs a develop copy of `harness`
* Listens for file systems events to convert notebooks to `python` scripts.


```python
%%script bash --bg
python setup.py develop
watchmedo tricks tricks.yaml
```

    Starting job # 2 in a separate thread.



```python
# Execute this cell to stop watching the files
%killbgscripts
```

    All background processes were killed.


### Build & Run Tests

The tests require `pytest` and `pytest-ipynb`.


```python
%%script bash
jupyter nbconvert harness/tests/*.ipynb --execute --to notebook --inplace 
py.test
```


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    //anaconda/lib/python3.5/site-packages/IPython/core/magics/script.py in shebang(self, line, cell)
        200         try:
    --> 201             out, err = p.communicate(cell)
        202         except KeyboardInterrupt:


    //anaconda/lib/python3.5/subprocess.py in communicate(self, input, timeout)
       1071             try:
    -> 1072                 stdout, stderr = self._communicate(input, endtime, timeout)
       1073             finally:


    //anaconda/lib/python3.5/subprocess.py in _communicate(self, input, endtime, orig_timeout)
       1714 
    -> 1715                     ready = selector.select(timeout)
       1716                     self._check_timeout(endtime, orig_timeout)


    //anaconda/lib/python3.5/selectors.py in select(self, timeout)
        375             try:
    --> 376                 fd_event_list = self._poll.poll(timeout)
        377             except InterruptedError:


    KeyboardInterrupt: 

    
    During handling of the above exception, another exception occurred:


    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-4-729201a5efa9> in <module>()
    ----> 1 get_ipython().run_cell_magic('script', 'bash', 'jupyter nbconvert harness/tests/*.ipynb --execute --to notebook --inplace \npy.test')
    

    //anaconda/lib/python3.5/site-packages/IPython/core/interactiveshell.py in run_cell_magic(self, magic_name, line, cell)
       2113             magic_arg_s = self.var_expand(line, stack_depth)
       2114             with self.builtin_trap:
    -> 2115                 result = fn(magic_arg_s, cell)
       2116             return result
       2117 


    <decorator-gen-106> in shebang(self, line, cell)


    //anaconda/lib/python3.5/site-packages/IPython/core/magic.py in <lambda>(f, *a, **k)
        186     # but it's overkill for just that one bit of state.
        187     def magic_deco(arg):
    --> 188         call = lambda f, *a, **k: f(*a, **k)
        189 
        190         if callable(arg):


    //anaconda/lib/python3.5/site-packages/IPython/core/magics/script.py in shebang(self, line, cell)
        203             try:
        204                 p.send_signal(signal.SIGINT)
    --> 205                 time.sleep(0.1)
        206                 if p.poll() is not None:
        207                     print("Process is interrupted.")


    KeyboardInterrupt: 



```python

```
