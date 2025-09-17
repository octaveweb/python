
# Decorator is a function that takes a function. then it create a new function in it own body (wrapper). then it returns the new function .

def decorator(func):
    def wrapper():
        print("I am about to excute a function")
        func()
        print("I have excuted this funtion")
    return wrapper

@decorator
def say_hello():
    print("Hello")
"""
F look like this:
def f():
        print("I am about to excute a function")
        say_hello()
        print("I have excuted this funtion")
f = decorator(say_hello)
f()
"""
say_hello()