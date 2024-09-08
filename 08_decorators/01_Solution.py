# Timming Function Excution
# Create a decorator that calculates the time of calculation of a function.

import time

def timer(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"{func.__name__} ran in {(end-start):.3f} sec.")
    return result
  return wrapper

@timer 
def example_func(n):
  time.sleep(n)

example_func(2)