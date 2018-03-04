to create a module in python, following is the directory structure
| -- package_name
   | -- __init__.py

A package is a special type of module that can contain other modules
The __init__.py file is the one which makes the package a module
The __init__.py file is executed when the package is executed
A package can contain sub-packages which contains __init__.py file


To import a class using the following statement
from PackageDirName.ModuleFilename import ClassNameInModuleFileName

Absolute import statement example
from PackageDirName.ModuleFilename import ClassNameInModuleFileName,ClassNameB
from PackageDirName.ModuleFilename import ClassNameInModuleFileName

Relative imports
used for importing items in the same top level package
Example:
my_pkg /
|--  __init__.py
|--  a.py
|__ subpkg
	|--  __init__.py
	|--  b.py
	|--  c.py 

to import module a and b from c, use the following relative syntax. This will reduce typing in deeply nested package struct
from ..a import A #the .. refers to the parent directory
from .b import B  #the . refers to the current directory

you can also use the foll. expression
from . import B #this will import themodule B in the current directory. However to refer to any classes inside module B, you have to use tge foll. ref
B.classname()



__all__ 
this is to specify the attribute names imported via "from moduleName import *", if not imports all public names from the import module
the __all__ is a list of strings which will be imported when import * is used

locals() 
function will show dict values of the local variables to their values. If __all__ is declared in __init__.py like below
example: __all__ = ['className','functionName']
this will only import the ones defined, Note: This wont prevent any of the module symbols (functions, classes etc) from being imported.
Note: Its recommened to import modules explicitly over wildcard

