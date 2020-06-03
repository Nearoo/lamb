import builtins, types
from .lamb import lamb

_builtins_tailed = {
    name + "_": val for name, val in builtins.__dict__.items() if callable(val) and name[0] != '_'
}

def __getattr__(name):
    if name in globals():
        return globals()[name]
    elif name in _builtins_tailed:
        def deferred(obj):
            if type(obj) == type(lamb):
                return obj._LambdaFactory__enchain(lambda a: _builtins_tailed[name](a))
            else:
                return _builtins_tailed[name](obj)
        return deferred

    elif name == "__all__":
        return list(globals()) + list(_builtins_tailed)
    else:
        raise AttributeError(name)
