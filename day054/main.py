import time
current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


def speed_calc_decorator(function):
    def wrapper_function():
        start = time.time()
        function()
        print(f"{function.__name__} run speed: {time.time() - start}")
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()
