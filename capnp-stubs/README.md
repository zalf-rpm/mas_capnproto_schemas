# capnp-stubs

Type stubs for [pycapnp](https://github.com/capnproto/pycapnp).

This package provides type information for the pycapnp library, enabling
static type checkers like mypy and Pyright to understand the Cap'n Proto
Python bindings.

## Important Note

**These stubs are for type checking only and should NOT be included in your runtime package distribution.**

The stubs should be kept separate from your main package to avoid conflicts with the actual pycapnp implementation.

## Usage

### For IDE / Type Checking (Development)

Your IDE (VS Code, PyCharm, etc.) will automatically use these stubs for type checking as long as they exist in the repository. No installation needed.

### For pycapnp Usage

pycapnp's public API is accessed via `capnp.lib.capnp`:

```python
from capnp.lib import capnp

# Now you can use all pycapnp functions:
capnp.load("schema.capnp")
capnp.run(my_coroutine())

# Or use the context manager:
with capnp.kj_loop():
    # Your async code here
    pass
```

## Methods Available

The stubs include all pycapnp 2.2.1 methods:
- `run()` - Run async coroutines with KJ event loop
- `kj_loop()` - Context manager for KJ event loop  
- `load()` - Load Cap'n Proto schema files
- `TwoPartyClient` / `TwoPartyServer` - RPC classes
- And many more...

## Methods NOT Yet Available

These methods are stubbed but not implemented in pycapnp 2.2.1:
- `getTimer()` - May be available in future versions
- `remove_event_loop()` - May be available in future versions

## Structure

The stub package provides:
- `capnp/__init__.pyi` - Main module stubs (type hints only, no `__init__.py`)
- `capnp/py.typed` - PEP 561 marker file
