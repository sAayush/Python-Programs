def log_function_call(func):
  def wrapper(*args, **kwargs):
    print(f"Calling function: {func.__name__}")
    return func(*args, **kwargs)
  return wrapper
def log_function_call2(func):
  def wrapper(*args, **kwargs):
    print(f"Calling function 2: {func.__name__}")
    return func(*args, **kwargs)
  return wrapper

@log_function_call
def greet(name):
  return f"Hello, {name}!"
@log_function_call2
def greet2(name):
  return f"Hello, {name}!"  

greeting = greet("Bob")
greeting2 = greet2("bobby")
print(greeting)  # Output: Calling function: greet
                  #        Hello, Bob!