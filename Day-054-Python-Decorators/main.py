import time 

def speed_calc_decorator(func):
    def wrapper_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"{func.__name__} run speed: {end_time - start_time}")
        return result
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i 
        
@speed_calc_decorator
def slow_function():
    for i in range(1000000):
        i * i
        
fast_function()
slow_function()