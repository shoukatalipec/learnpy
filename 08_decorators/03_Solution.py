# Cache Return Values
# Implement a decorator that cashes the return values of a fnction, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function
import time

def cache(func):
  cache_value = {}
  print(cache_value)
  def wrapper(*args):
    if args in cache_value:
      return cache_value[args]
    result = func(*args)
    cache_value[args] = result
    return result
  return wrapper

@cache
def long_run_func(a, b):
  time.sleep(2)
  return a + b

long_run_func(2,3)
long_run_func(5,3)