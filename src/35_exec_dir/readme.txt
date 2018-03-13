exec dirs are directories containing an entry point for python execution
usually if a python module is passed as argument, it will complin like this

python path_to_pckage

python can't find '__main__' module in 'path_to_package' is because the __main__.py is missing in the root directory

To execute python executable call

#note the \* is to escape symbol
python calc 2 \* 5
python calc 2 - 5
python calc 2 + 5


#distributing executable
zip the contents in the top level directory containing __main__.py
zip -r ../calc.zip *

execute commands with ref to zip file
python calc.zip 1 + 1


#prj structure
| project_name
| -- __main__.py --> required only if the project needs to be executable
| --|
|   | -- project_name
|        | 
|		 | -- __init__.py
|		 | -- module1.py
|		 | -- test
|			  | -- __init__.py
|			  | -- unit_test.py
| -- setup.py	 

