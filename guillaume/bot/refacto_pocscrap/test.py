from time import time, sleep

def timer(func):
    def f(x, y=10):
        before = time()
        result = func(x, y)
        after = time()
        print("Le temps que ça a pris : {}".format(after - before))
        return result
    return f

@timer
def add(x, y=10):
    for i in range(x):
        sleep(1)
    return x + y

@timer
def sub(x, y=10):
    for i in range(x):
        sleep(1)
    return x - y
    
print("sub(10)", sub(10))