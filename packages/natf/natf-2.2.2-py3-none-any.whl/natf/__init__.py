import os
from warnings import warn

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'version')) as f:
    version = f.read().strip()
__version__ = version

if os.name == 'nt':
    p = os.environ['PATH'].split(';')
    lib = os.path.join(os.path.split(__file__)[0], 'lib')
    os.environ['PATH'] = ";".join([lib] + p)
