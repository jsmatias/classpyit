# ClassPyIt

[This module is still in initial stage]
Want to collaborate to it? You're more than welcome. 

Simple module to make an object from dictionary

To make it global, move it to /User/username/Library/Python/3.x/lib/python/site-packages/

To check the list of all the possible paths, which you can store the file in, run the following code in a python shell:

```
import sys
sys.path
```

# Usage

Ex.:

```
from classipyit import ClassPyIt

d = {'Say Hi': lambda: print('Hello world'), 'age': 2, 0: 'int as a key is replaced by N<int>'}

dObj = ClassPyIt(d)

>> print(dObj.SayHi())
Hello World

>> print(dObj.N0)
'int as a key is replaced by N<int>'

```
