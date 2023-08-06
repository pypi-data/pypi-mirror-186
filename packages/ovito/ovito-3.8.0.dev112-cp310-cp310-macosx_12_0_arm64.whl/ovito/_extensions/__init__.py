import pkgutil
import importlib

# Load all plugin extension modules in this package.
for modinfo in pkgutil.walk_packages(__path__, __name__ + '.'):
    importlib.import_module(modinfo.name)

# Load the Python-based extension scripts.
import ovito._extensions.scripts.modifiers
import ovito._extensions.scripts.readers