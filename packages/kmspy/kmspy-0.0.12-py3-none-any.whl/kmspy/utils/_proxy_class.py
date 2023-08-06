changer_methods = set("__setitem__ __setslice__ __delitem__ update append extend add insert pop popitem remove setdefault __iadd__".split())


def _callback_getter(obj):
    def callback(name):
        obj._has_changed = True
    return callback

def _proxy_decorator(func, callback):
    def wrapper(*args, **kw):
        callback(func.__name__)
        return func(*args, **kw)
    wrapper.__name__ = func.__name__
    return wrapper

def _proxy_class(cls, obj):
    new_dct = cls.__dict__.copy()
    for key, value in new_dct.items():
        if key in changer_methods:
            new_dct[key] = _proxy_decorator(value, _callback_getter(obj))
    return type("proxy_"+ cls.__name__, (cls,), new_dct)


if __name__ == "__main__":
    class Flag(object):
        def __init__(self):
            self.clear()
        def clear(self):
            self._has_changed = False

    flag = Flag()
    NotifierList = _proxy_class(list, flag)