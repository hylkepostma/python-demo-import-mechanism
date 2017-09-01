# Python Demo Import Mechanism

Example package demonstrating the Python import mechanism.

[TOC]

## Getting started

`git clone `



## Example #1: Command line

When inside the repository's root folder (`<path_to>\demo-import-mechanism`) you can run Python code loaded as a module (using `python -m`) on the **command line**, like so:

`python -m mypackage.main` to run `mypackage\main.py`

*or*

`python -m mypackage.module_one` to run `mypackage\module_one.py`

*or*

` python -m mypackage.mychildpackage.module_one` to run `mypackage\mychildpackage\module_one.py`



## Example #2: Importing

You can install this package using `pip`:

```
pip install <path_to>\demo-import-mechanism
```

Now you can use the Python code by **importing** it, like so:

```
import mypackage.main
mypackage.main.test()
```

*or*

```
from mypackage import module_one
module_one.test()
```

*or*

```
import mypackage.mychildpackage.main as short_name
short_name.test()
```

*or*

```
from mypackage.mychildpackage import module_one
test_object = module_one.Test()
test_object.test()
```



## Example #3: Frozen executable

You can safely build a **frozen executable** from this package using the `python-exe-builder`. For more information see: https://bitbucket.org/hylkepostma/python-exe-builder



*Using PowerShell*

Activate `python-exe-builder`'s venv:

```
<path_to>\python-exe-builder\venv\Scripts\activate.ps1
```
Run python-exe-builder:
```
python <path_to>\python-exe-builder\src\builder.py <path_to>\demo-import-mechanism --onefile --src_folder=mypackage
```
Deactivate `python-exe-builder`'s venv:
```
deactivate
```



## Example #4: Python Package Index

We can also make a package ready for uploading to the **Python Package Index** (**PyPI**), using `wheel` and ` twine`.



*Using PowerShell*

Activate `demo-import-mechanism`'s venv:
```
<path_to>\demo-import-mechanism\venv\Scripts\activate.ps1
```
Install dependencies:
```
pip install wheel
pip install twine
```
Create some different distributions:
```
python setup.py sdist --formats=gztar,zip bdist_wheel
```
Upload package to PyPI with `twine`:
```
twine upload dist/<choose_distribution>
```
Deactivate `demo-import-mechanism`'s venv:
```
deactivate
```



Note: now you can also install the package from a distribution using `pip`. For example, like so: `pip install <path_to>\demo-import-mechanism\dist\demo_import_mechanism-0.1-py3-none-any.whl`



## Terminology

At the risk of stating the obvious, some explanation of common used Python terminology.

- A Python module is simply a Python source file (.py), which can expose classes, functions and global variables.

- A Python package is simply a directory of Python module(s). A file called `__init__.py` tells Python to treat the directory as a package.

  ​



## Naming conventions

* Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. 
* Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.





## Sources

https://softwareengineering.stackexchange.com/a/111882

https://stackoverflow.com/a/14132912

https://www.python.org/dev/peps/pep-0008/#package-and-module-names