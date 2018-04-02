Namespace packages splits packages across several directories
They have no __init__.py
this avoid complex init problems

How python finds namespace packages
1. Python scans each of the entries in sys.path
2. if a matching folder name is found for the packagename with __init__.py, then a normal package is loaded
3. if a module is found eg. foo.py the name python is looking for is found, then this is loaded
4. otherwise all matching directories in sys.path are considered part of the namespace package

If two namespace packages contains the same module name, then the last import statement overrides the first one
Example:


|-- Pkg1
    |-- myfarm
        |-- cow
            |-- cow.py (This class has two methods wakeup and sleep)

|-- Pkg2
    |-- myfarm
        |-- cow
            |-- cow.py (this class has only one method wakeup)

from pkg1.myfarm.cow.cow import Cow
dir(Cow) will list wakeup and sleep

from pkg2.myfarm.cow.cow import Cow
dir(Cow) will list only wakeup

Solution: if there is name conflicts in module name, use alias
from pkg1.myfarm.cow.cow import Cow as c1
from pkg2.myfarm.cow.cow import Cow as c2


