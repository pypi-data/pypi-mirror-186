from . import search
from . import graph
from . import helpers
from . import fs
from . import io
from . import nums
from . import structures

__version__ = "0.9.1"

# constants
phi = 1.618033988749895


def randcolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
