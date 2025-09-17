
def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper 
    return decorator

@repeat(7)
def say_hello(name):
    print(f"Hello! {name}")

'''
It replaces the function say_hello with this:
def decorator(func):
    def wrapper(a):
        for i in range(n):
            say_hello(a)
    return wrapper
'''

say_hello("Harry")


# n = int(input("Enter number of print: "))

# def repeat():
#     print("Hello - Karan")

# for i in range(0, n):
#     repeat()
    