#!/usr/bin/env python2

print "Hello, shebang demo"

## The shebang line in any script determines the script's ability to be executed like an standalone executable without typing python beforehand in the terminal or when double clicking it in a file manager (when configured properly)

#Correct usage for Python 3 scripts is
#!/usr/bin/env python3

#Correct usage for Python 2 scripts is
#!/usr/bin/env python2

#Following should NOT be used, as python can refer either to python2 or python3 on different systems. If at all being used, ensure the code works both on Python2 and Python3
#!/usr/bin/env python

#DO NOT Use the following, as python may be installed at /usr/bin/python or /bin/python in those cases, the above #! will fail.
#!/usr/local/bin/python


