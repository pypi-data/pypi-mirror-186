# Nested Inside

The `Nested Inside` package provides a nested data structure that allows for easy and intuitive access and modification of nested data. The package defines a `Nested` class that wraps a data structure (e.g. a dictionary, list, or tuple) and allows for nested access using a specified delimiter (default "->"). The class provides several methods such as `get`, `set`, `parse` to access and modify the nested data, and also provides derived classes such as `NestedDict`, `NestedList`, and `NestedTuple` to return the data in a modifiable or immutable format. This package can be especially useful when working with complex data structures that contain multiple nested levels, as it allows you to access and modify the data using a simple key path instead of having to navigate through multiple levels of nested data manually.

## Installation

To install the package, use pip:

```
pip install nested_inside
```


## Usage

The package provides a `Nested` class that wraps a data structure (e.g. a dictionary, list, or tuple) and allows for nested access using a specified delimiter (default "->").

```python
from nested_inside import NestedDict

data = {
    "a": {
        "b": [1, 2, 3],
        "c": "hello"
    }
}
nested_data = NestedDict(data)

# Accessing nested values using get function
value = nested_data.get("a->b->0")
print(value) # 1

# Modifying nested values using set function
nested_data.set("a->b->0", 4)
# modify or access data using [] syntax
nested_data['a->b->1'] = 3
# modify or access data using object call
nested_data('a->b->2', 4)
# modify or access data using dot notation
nested_data.a.c = "world"

print(nested_data.a.b) # [4, 3, 4]
# call object without any parameter to retrieve data
print(nested_data('a->c'))

# Retrieving default value by providing value to default
value = nested_data("a->d", default="not found")
print(value) # "not found"

# Return mutable object
value = nested_data.get("a", modify=True)
# provide tuple as key to modify
value[["b"]] = [5, 6, 7]

# provide tuple as key
print(nested_data.get(("a","b"))) # [5, 6, 7]

# provide list as key
print(nested_data[["a","b", 2]]) # 7

# provide list as key with index as string
print(nested_data[["a","b", "0"]]) # 5

```

## Methods

- `__init__(self, data: Any, delimiter: str = "->")`: Initialize a new Nested object with the given data and delimiter.
- `parse(self, value: Any, modify: bool = False) -> Any`: A helper function that converts the value to a modifiable or immutable object based on the 'modify' flag
- `get(self, key: Union[int, str, list, tuple, None], default=NODEFAULT, modify: bool = False) -> Any`: Retrieves the value stored at the specified key path in the nested data structure.
- `set(self, key: Union[int, str, list, tuple], value: Any) -> None`: Set the value stored at the specified key path in the nested data structure.

## Contributing

If you would like to contribute to the package, feel free to submit a pull request.

## License

The package is licensed under the MIT License.

