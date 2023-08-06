import datetime

from .helpers import take_screenshot

def print_fn(func):
    # Getting the argument names of the
    # called function
    argnames = func.__code__.co_varnames[:func.__code__.co_argcount]
    
    # Getting the Function name of the
    # called function
    fname = func.__name__
    
    def wrapper(*args, **kwargs):
        print(fname, "(", end = "")
        # printing the function arguments
        print(', '.join( '% s = % r' % entry for entry in zip(argnames[1:], args[1:len(argnames)])), end = ", ")
        
        # Printing the variable length Arguments
        # print("args =", list(args[len(argnames):]), end = ", ")
        
        # Printing the variable length keyword
        # arguments
        print("kwargs =", kwargs, end = "")
        print(")")
        
        return func(*args, **kwargs)
    
    return wrapper

def confirm_output_eq(value, on_success_message:str="Success", on_failure_message:str="Failure"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                assert func(*args, **kwargs) == value
                print(on_success_message)
            except AssertionError:
                print(on_failure_message)
        return wrapper
    return decorator

def confirm_output_contains(value, on_success_message:str="Success", on_failure_message:str="Failure"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                assert value in func(*args, **kwargs)
                print(on_success_message)
            except AssertionError:
                print(on_failure_message)
        return wrapper
    return decorator


def screenshot_step(screenshot_name:str=None, when:str='before'):
    def decorator(func):
        argnames = func.__code__.co_varnames[:func.__code__.co_argcount]
        fname = func.__name__
        def wrapper(*args, **kwargs):
            if screenshot_name is None:
                screenshot_name = fname
            driver = args[0].driver
            if when == 'before':
                take_screenshot(driver, screenshot_name)
                val = func(*args, **kwargs)
                return val
            elif when == 'after':
                val = func(*args, **kwargs)
                take_screenshot(driver, screenshot_name)
                return val
        return wrapper
    return decorator

def screenshot_before(func):
    argnames = func.__code__.co_varnames[:func.__code__.co_argcount]
    fname = func.__name__
    def inner_func(*args, **kwargs):                
        val = func(*args, **kwargs)
        assert "context" == argnames[0]
        driver = args[0].driver
        take_screenshot(driver, fname)
        return val
    return inner_func

def screenshot_after(func):
    argnames = func.__code__.co_varnames[:func.__code__.co_argcount]
    fname = func.__name__
    def inner_func(*args, **kwargs):                
        assert "context" == argnames[0]
        driver = args[0].driver
        take_screenshot(driver, fname)
        val = func(*args, **kwargs)
        return val
    return inner_func


def ext_step(func):
    pass