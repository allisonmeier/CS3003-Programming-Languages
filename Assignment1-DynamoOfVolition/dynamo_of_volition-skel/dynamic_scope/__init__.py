from typing import Dict, Any, Iterator, Optional
from collections import abc
from types import FunctionType
import inspect

# stuff to complete: 
# return a DynamicScope object (have to define and implement that class also)
# DynamicClass has to support associative lookup operations (ie work like a python dictionary)
# if user indexes a DynamicScope object using a var name not bound in the object, raise NameError exception


class DynamicScope(abc.Mapping):
    def __init__(self):
        self.env: Dict[str, Optional[Any]] = {}


def get_dynamic_re() -> DynamicScope:
    return None
