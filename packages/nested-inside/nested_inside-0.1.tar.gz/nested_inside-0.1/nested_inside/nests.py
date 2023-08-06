from typing import Union, List, Tuple, Any

NODEFAULT = "THROWERROR"

class Nested:
    def __init__(self, data: Any, delimiter: str = "->"):
        """
        Initialize a new Nested object with the given data and delimiter.

        :param data: The initial data to be stored in the nested data structure.
        :param delimiter: The string that separates keys in the key path when accessing nested values. Default is "->".
        """
        self._parent = None
        super().__init__(data)
        self._delimiter = delimiter

    def parse(self, value: Any, modify: bool = False) -> Any:
        """
        A helper function that converts the value to a modifiable or immutable object based on the 'modify' flag

        :param value: The value that needs to be converted.
        :param modify: A flag that indicates whether the returned value should be a modifiable object or not. If set to True, the returned value will
                      be the same as the input value. Otherwise, it will be an instance of NestedDict, NestedList or NestedTuple.
                      Default is False.
        :return: The converted value.
        """
        if modify:
            return value
        if isinstance(value, dict):
            value = NestedDict(value, self._delimiter)
            value._parent = self
        elif isinstance(value, list):
            value = NestedList(value, self._delimiter)
            value._parent = self
        elif isinstance(value, tuple):
            value = NestedTuple(value, self._delimiter)
            value._parent = self
        return value

    def get(self, key: Union[int, str, list, tuple, None], default=NODEFAULT, modify: bool = False) -> Any:
        """
        Retrieves the value stored at the specified key path in the nested data structure.
        If the key is not found and default is not provided, raises an error.
        If the key is not found and default is provided, returns default.

        :param key: The key path to the desired value in the nested data structure, using the delimiter defined in the __init__ method.
                    It can be of type str, list or tuple.
        :param default: The value to return if the key is not found in the nested data structure. Default is NODEFAULT.
        :param modify:  A flag that indicates whether the returned value should be a modifiable object or not. If set to True, the returned value will
                        be the same as the input value. Otherwise, it will be an instance of NestedDict, NestedList or NestedTuple.
                        Default is False.
        :return: The value stored at the specified key path in the nested data structure.
        """

        if not key:
            return self.parse(self, modify)
        try:
            if isinstance(key, (str, list, tuple)):
                self._key = key
                keys = key.split(self._delimiter) if isinstance(key, str) else key
                value = self
                for k in keys:
                    if isinstance(value, (list, tuple)):
                        if isinstance(k, int) or k.isdigit():
                            value = value[int(k)]
                        else:
                            value = value[self._get_list_index(k, value)]
                    else:
                        if isinstance(k, str) and k.isdigit() and int(k) in value.keys():
                            value = value[int(k)]
                        else:
                            value = value[k]
            elif isinstance(key, int):
                value = self[key]
            else:
                raise SyntaxError(f"Key of type {key.__class__.__name__} is not supported")
        except (AttributeError, IndexError, KeyError) as e:
            if default == NODEFAULT:
                raise e
            return default
        
        return self.parse(value, modify)

    def set(self, key: Union[int, str, list, tuple], value: Any) -> None:
        """
        Set the value stored at the specified key path in the nested data structure.

        :param key: The key path to the desired value in the nested data structure, using the delimiter defined in the __init__ method.
                    It can be of type str, list or tuple.
        :param value: The value to be set at the specified key path.
        """

        self.__setitem__(key, value)
    
    def _get_list_index(self, key: Union[int, str], lst: list) -> int:
        """
        A helper function that finds the index of the key in the given list of dictionaries.

        :param key: The key to be searched in the list of dictionaries.
        :param lst: The list of dictionaries in which the key needs to be searched.
        :return: The index of the key in the given list of dictionaries.
        """

        for i, d in enumerate(lst):
            if isinstance(d, dict) and key in d:
                return i
        raise KeyError
    
    def __call__(self, key: Any = None, value: Any = None, default=NODEFAULT) -> Any:
        """
        Allows the class instance to be called as a function.
        When called with a key, it returns the value stored at the specified key path in the nested data structure.
        If the key is not found and default is not provided, raises an error.
        If the key is not found and default is provided, returns default.
        When called with a key and a value, it sets the value stored at the specified key path in the nested data structure.
        When called without any arguments, it returns the entire nested data structure.

        :param key: The key path to the desired value in the nested data structure, using the delimiter defined in the __init__ method.
                    It can be of type str, list or tuple.
        :param value: The value to be set at the specified key path.
        :param default: The value to return if the key is not found in the nested data structure. Default is NODEFAULT.
        :return: The value stored at the specified key path in the nested data structure.
        """

        if value:
            return self.set(key, value)
        else:
            return self.get(key, default)
    
    def __getitem__(self, key: Union[str, int, list, tuple]) -> Any:
        """
        Retrieves the value stored at the specified key path in the nested data structure using the [] operator.

        :param key: The key path to the desired value in the nested data structure, using the delimiter defined in the __init__ method.
                    It can be of type str, int, list or tuple.
        :return: The value stored at the specified key path in the nested data structure.
        """

        if (isinstance(key, str) and self._delimiter in key) or isinstance(key, (list, tuple)):
                return self.get(key)
        return super().__getitem__(key)

    def __setitem__(self, key: Union[str, int, list, tuple], value: Any) -> None:
        """
        Set the value stored at the specified key path in the nested data structure using the [] operator.

        :param key: The key path to the desired value in the nested data structure, using the delimiter defined in the __init__ method.
                    It can be of type str, int, list or tuple.
        :param value: The value to be set at the specified key path.
        """
        if (isinstance(key, str) and self._delimiter in key) or isinstance(key, (list, tuple)):
            keys = key.split(self._delimiter) if isinstance(key, str) else key
            d = self.get(self._delimiter.join(keys[:-1]), modify=True)
            if isinstance(d, (list, tuple)) and keys[-1].isdigit():
                d[int(keys[-1])] = value
            else:
                d[keys[-1]] = value
        else:
            super().__setitem__(key, value)
    def __getattr__(self, key: str) -> Any:
        """
        Retrieves the value stored at the specified key path in the nested data structure using dot notation.

        :param key: The key path to the desired value in the nested data structure, using the delimiter defined in the __init__ method.
        :return: The value stored at the specified key path in the nested data structure.
        """
        try:
            return self.get(key)
        except KeyError:
            raise AttributeError(key)
    def __setattr__(self, key: str, value: Any) -> None:
        """
        Set the value stored at the specified key path in the nested data structure using dot notation.

        :param key: The key path to the desired value in the nested data structure, using the delimiter defined in the __init__ method.
        :param value: The value to be set at the specified key path.
        """
        if key not in ['_parent', '_key', '_delimiter']:
            if self._parent and self._parent._key:
                if isinstance(self._parent._key, str):
                    key = self._delimiter.join([self._parent._key, key])
                else:
                    key = self._parent._key
                self._parent[key] = value
            else:
                self[key] = value
        else:
            super().__setattr__(key, value)
        

class NestedDict(Nested, dict):
    pass 

class NestedList(Nested, list):
    pass

class NestedTuple(Nested, tuple):
    pass
