# Debugging Function Calls
# Create a decroator that prints function name and the value sot its arguments every time it is called

def debug(func):
  def wrapper(*args, **kwargs):
    args_value = ', '.join(str(arg) for arg in args)
    kwargs_value = ', '.join(f"{k},{v}" for k, v in kwargs.items())
    print(f"Calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}.")
    return func(*args, **kwargs)
  return wrapper

@debug
def hello(user):
  print(f"Hello!, {user}")

@debug 
def greet(name, greeting="Hello"):
  print(f"{greeting}, {name}")


hello("Shoukat Ali")
greet("Shoukat",greeting="Good Morning")