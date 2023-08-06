b26 - Base 26 Encoder and Decoder
=================================

A common example usage is alphabetical counting:
When 'Z' is reached, the next items will be 'AA',
'AB' and so on.


Installation
------------

```bash
pip install b26
```


Basic Usage
-----------

```python
import b26

for i, item in enumerate([
    "Apples",
    "Banana",
    "Pineapple",
    ...,
]):
    print(f"{b26.encode(i)}. {item}")
```

API
---

### `decode()`

```python
decode(string: str) -> int
```

_Converts an alphabetical string into an integer._

#### Parameters
__string__
_A string that only consists of ASCII letters to
convert into an integer._


### `encode()`

```python
encode(integer: int) -> str
```

_Convert an integer into an alphabetical string._

#### Parameters

__integer__
_A positive integer or 0 to convert into a
string._
    
#### Returns

_An uppercase alphabetical string._

