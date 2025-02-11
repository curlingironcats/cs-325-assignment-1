def decorator_example(func):
    def wrapper():
        print("Before the function call.")
        func()  # original function
        print("After the function call.")
    return wrapper

@decorator_example
def hello_world():
    print("Hey, github!")

hello_world()
