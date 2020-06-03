from lamb import *
from lamb.builtins_ import *
from lamb.varnames_ import *

g = lamb + 2 > 3
f = filter_(g, lamb)


print(f(range(20)))
