# Lamb: Concise lambda generation

This module introduces a single new object called `lamb` that can be used to create single-argument lambda methods in a more concise and clear manner.


For instance, to create a function that adds two to an object, the following lines are sufficient:

    >>> f = lamb + 2
    >>> print(f(4))
    6


Arithmetic operations can also be chained to create more complex expressions:

    >>> f = (lamb ** 2 + 30) % 3 == 10
    >>> f(5)
    True

To chain arbitrary functions, the rightshift (`>>`) operator can be used:

    >>> a = lambda x: x + 2
    >>> b = lambda y: y * 3
    >>> g = (lamb + 3) >> a >> b
    >>> g(4)
    27

`lamb` can also be used to create functions applicable on class instances; getting attributes, for instance, is as easy as it sounds:

    >>> class A:
            def x(self):
                return 3
    >>> f = lamb.x() * 4
    >>> a = A()
    >>> f(a)
    12

Builting functions have a very strict policy in terms of return types, so they could not be overloaded