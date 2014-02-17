from functools import wraps
from inspect import isfunction

class Registry(object):
    
    _r = dict()
    
    @classmethod
    def register(cls,for_class,impl):
        cls._r[for_class.__name__] = impl
    
    @classmethod
    def get_instance(cls,for_class,*args,**kwargs):
        satisfies = cls._r[for_class.__name__]
        #if isfunction(satisfies) or isinstance(satisfies,type):
        #    return satisfies(*args,**kwargs)
        if callable(satisfies):
            return satisfies(*args,**kwargs)
            
        return satisfies
    
    @classmethod
    def clear(cls):
        cls._r = dict()
        
    
def dependency(cls):
    def x(fn):
        @wraps(fn)
        def y(inst,*args,**kwargs):
            return Registry.get_instance(cls,*args,**kwargs)
        return y
    return x