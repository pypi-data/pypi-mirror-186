import functools

def compose(g, f):
    def h(*args):
        return g(f(*args))
    return h


def compose_bis(g, f):
    def h(x):
        return g(f(x))
    return h

def compose_3(h, g, f):
    def i(*args):
        return h(g(f(*args)))
    return i


def compose_4(i, h, g, f):
    def j(*args):
        return i(h(g(f(*args))))
    return j

def compose_5(j, i, h, g, f):
    def k(*args):
        return j(i(h(g(f(*args)))))
    return k


def compose_f_input(g, f):
    def h():
        return g(f())
    return h

def convert_to_filter(fn):
    @functools.wraps(fn)
    def wrapper(entry):
        return filter(fn, entry)
    return wrapper


def convert_to_map(fn):
    @functools.wraps(fn)
    def wrapper(entry):
        return map(fn, entry)
    return wrapper
