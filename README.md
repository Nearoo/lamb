# Lamb 🐑: Concise Function Description in Python


```python
from lamb import *
```

## Introduction

This module allows to express simple functions in a compact and intuitive way using a single object called `lamb`. 


`lamb`s can be thought of as placeholder for variables inside an expression. The expression can then be evaluated as if it was a function, where each `lamb` gets replaced with a function argument.

For instance, the following line filters all elements from a list who's `mod-4` equivalence is not greater than 2:


```python
filtered = filter(lamb % 4 > 2, range(10))

print(list(filtered))
```

## Arithmetic and Boolean Operators
Arithmetic operations and boolean comparators can also be freely chained together to create more complex expressions:


```python
f = (lamb ** 2 + 30) % 15 == 10

f(5)
```

## Function Chaining
There is also the possibility to chain arbitrary functions. The rightshift operator (`>>`) is overloaded such that if it is called with functions as arguments, it chains them together:


```python
def a(x):
    return x + 2

def b(y):
    return y * 3

g = (lamb >> a >> b) % 4

g(4)
```




    2



## Attribute, Methods and Indexes
`lamb` can also be used to create functions applicable on class instances; getting attributes, calling methods or accessing  indexed data works as would intuitively be expected:


```python
class A:
    def x(self):
        return [1, 2, 3]
    

f = lamb.x()[2]

f(A())
```




    3



## Applying builting functions
To apply builtin functions to an object, `lamb` provides a submodule containing deferred versions of all builtin functions. They can be invoked by writing the original function name but with a trailing underscore `_`:


```python
from lamb.builtins_ import *

a = {1:2}
l = list_(lamb.values())

print(l(a))
```

    [2]


## Multi-Lamb Expressions, Dynamic Lamb Generators
There can also be multiple lambs in a single expression. When called, arguments are then applied to the lambs from left to right. This can be slightly confusing, since intuitively, lambs look like variables, and the same variable should get the same value. It's thus a good idea to rename the lambs to different variable names.


```python
x = y = z = lamb
f = (x + y) * z
f(1, 2, 3)
```




    9



But writing `x = y = z = lamb` each time a new multi-lamb expression is created is a bit tedious and the defeats the purpose of lambs overall. There's thus a submodule called `vs` provided that generates lamb-names for all letters in the alphabet. To avoid name-clashes in the current namespace, we can dynamically add pre- and postfixes to all lamb-names by adding pre- and postfixes to the module name `vs`:


```python
from lamb.vs import *
print(a, b, c, x, y, z)

from lamb.__vs_pfix import *
from lamb.obj_vs import *

print(__a_pfix, __c_pfix, obj_a, obj_b)
```

    🐑 🐑 🐑 🐑 🐑 🐑
    🐑 🐑 🐑 🐑


## Partial Application
Partial application is possible as well. Nothing is required but calling with fewer arguments.


```python
f = (x + y) * z

print(f(1, 2)(3))
```

    9

