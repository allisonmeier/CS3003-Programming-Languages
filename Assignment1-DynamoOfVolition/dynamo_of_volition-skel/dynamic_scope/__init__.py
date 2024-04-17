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
        
        return self.env[key]

    def __setitem__(self, key: str, value):
        self.env[key] = value

    def __len__(self): 
        return __len__(self.env) #FYI: fact that __len__ isn't defined isn't causing problems. just ignore
    
    def __iter__(self) -> Iterator:
        return self.env.__iter__()


def get_dynamic_re() -> DynamicScope:

    stackDict = DynamicScope() # object, dict of whatever is in the applicable stack

    stackList = inspect.stack() # list of all the stuff in the stack, in order 
    stackList = stackList[1:] # cut off the first item in the list (just a bunch of loud, wordy info that I don't need)

    

    for itemInStackInfo in stackList:
        #print(itemInStackInfo.frame.f_locals)
        freeVariablesList = list(itemInStackInfo.frame.f_code.co_freevars)

        for individualInfo in itemInStackInfo.frame.f_locals:
            #print(x)
            #print(itemInStackInfo.frame.f_locals[individualInfo])
            #if individualInfo in freeVariablesList:
                #print(f'HEY THERES A FREE VAR RIGHT HERE CALLED {individualInfo}')

            if not individualInfo in stackDict.env and not individualInfo in freeVariablesList:
                #print("not here")
                stackDict.env[individualInfo] = itemInStackInfo.frame.f_locals[individualInfo]
            #else:
                #print("duplicate")

        for item in stackDict:
            if item in freeVariablesList:
                print(f'You missed a free variable called {item} at {stackDict[item]}')

    return stackDict
