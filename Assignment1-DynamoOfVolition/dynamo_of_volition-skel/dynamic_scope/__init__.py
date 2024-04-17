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

    def __getitem__(self, key: str):
        if not key in self.env:
            raise NameError
        if self.env[key] == '__unbound__':
            raise UnboundLocalError('Unbound Local error boooo')
        return self.env[key]

    def __setitem__(self, key: str, value):
        self.env[key] = value

    def __len__(self): 
        return self.env[1:] 
    
    def __iter__(self) -> Iterator:
        return self.env.__iter__()

def get_dynamic_re() -> DynamicScope:

    stackScope = DynamicScope() # object, dict of whatever is in the applicable stack

    stackList = inspect.stack() # list of all the stuff in the stack, in order 

    # cut off the first item in the list (just a bunch of loud, wordy info that I don't need)
    for stackItem in stackList[1:]:
        freeVars = list(stackItem.frame.f_code.co_freevars)
        localVars = stackItem.frame.f_locals
        
        everyVarInclUnboundOnes = list(stackItem.frame.f_code.co_cellvars + stackItem.frame.f_code.co_varnames)

        for infoStr in localVars:
            # if infoStr isn't already listed in the stack dict strings, deal with that by adding it in.
                # also, filter out free variables 
            if not infoStr in stackScope.env and not infoStr in freeVars:
                #print("not here")
                stackScope.env[infoStr] = localVars[infoStr]

        # FYI to help ID any sneaky free variables
        for item in stackScope:
            if item in freeVars:
                print(f'You missed a free variable called {item} at {stackScope[item]}')
        
        # make sure there's no local vars messing around still
            # and that the list of every single var actually exists 
        if len(localVars)==0 and len(everyVarInclUnboundOnes)>0:
            for var in everyVarInclUnboundOnes:
                # the only stuff left must be unbound
                stackScope[var] = '__unbound__'

    return stackScope
