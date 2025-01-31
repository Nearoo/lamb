#%%
from lamb import *
#%% Primary purpose: Create small anonymous functions
res = filter(lamb % 5 < 3, range(30))

#%% Arbitrary arithmetic and boolean operators are allowed:
f   = (lamb ** 2 % 6) - 28 != 5 / 4
f_l = lambda x: (x ** 2 % 6) - 28 != 5 / 4
f(2) == f_l(2) # The two expressions are equivalent

#%% Empty function calls, index and attribute access are possible as well
g = lamb().x[2] - 3 == 0

#%% Lambs can be chained with other functions using the righshift operator
h = g >> f >> lamb + 2 # make sure the first function is a lamb

#%% For multi-variable lambs, different lamb names improve clarity
from lamb.vs import * # Imports a, b, c, ..., z
from lamb.l_vs_ import * # Import l_a_, l_b_, l_c_... arbitrary pre- and postfixes are possible
g = (l_a_ - b) * c

#%% g is now a function of three arguments, or rather: functions returning functions, with one arg each (shoutout to Haskell)
g(1)(2)(3) == g(1, 2)(3) == g(1, 2, 3)
#%% Arguments replace lambs left-to-right:
g(1, 2, 3)
# OUTPUT: -3

#%% Note that `a_ is b_` and `a_ is lamb`; they differ only in their identifier, so the following are equivalent:
g2 = (lamb - lamb) * lamb
g(1, 2, 3) == g2(1, 2, 3)

#%% Lambs can be nested. Parents inherit un-evaluated lambs from their children.
# For clarity, lambs can be added as placeholder for unevaluated args:
h  = g(1, 2) + g(3) 
h2 = g(1, 2, a) + g(3, a, b)
h(1, 2, 3) == h2(1, 2, 3)

#%% In a select few cases, this will work, but is discouraged. Use g = lamb >> f instead.
f = lambda x: x + 2 == 5
g = f(lamb)
f(2) == g(2)
