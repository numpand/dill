from dill.temp import dump, dump_source, dumpIO, dumpIO_source
from dill.temp import load, load_source, loadIO, loadIO_source


f = lambda x: x**2
x = [1,2,3,4,5]

# source code to tempfile
pyfile = dump_source(f, alias='_f')
_f = load_source(pyfile)
assert _f(4) == f(4)

# source code to stream
pyfile = dumpIO_source(f, alias='_f')
_f = loadIO_source(pyfile)
assert _f(4) == f(4)

# pickle to tempfile
dumpfile = dump(x)
_x = load(dumpfile)
assert _x == x

# pickle to stream
dumpfile = dumpIO(x)
_x = loadIO(dumpfile)
assert _x == x

