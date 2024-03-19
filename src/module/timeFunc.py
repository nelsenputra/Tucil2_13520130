from functools import wraps
from time import perf_counter

def timeHere(func): 
    def wrapFunc(*args, **kwargs): 
        t1 = perf_counter() 
        result = func(*args, **kwargs) 
        t2 = perf_counter() 
        print(f'\nExecution time: {1000*(t2-t1):.2f}ms') 
        return result 
    return wrapFunc