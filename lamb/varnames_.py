
import string
from .lamb import lamb

_varnames = list(map(lamb + "_", string.ascii_lowercase))

def __getattr__(name):
    if name in globals():
        return globals()[name]
    elif name in _varnames:
        return lamb
    elif name == "__all__":
        return list(globals()) + list(_varnames)
    else:
        raise AttributeError(name)
