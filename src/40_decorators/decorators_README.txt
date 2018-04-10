decorators must can be callable objects including
1. Functions
2. Classe Definition - the class ctor (__init__) will be called to pass the function reference and the callable (__call__) must return the function return value
3. Class Instance - here the class callable (__call__) will be used to pass the function and return the function results
