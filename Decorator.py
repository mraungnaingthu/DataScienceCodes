import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() #Record start time
        result = func(*args, **kwargs)
        end_time = time.time() #Record end time
        print(f"Function '{func.__name__}' took {end_time - start_time:.5f}")
        return result
    return wrapper

@log_execution_time
def slow_function():
    time.sleep(2)
    return "Finished"

@log_execution_time
def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    print(slow_function())
    print(add_numbers(1, 2))
