def catchableConnection(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print("Un problème est apparu avec la connexion...")
 
    return wrapper

def timer(func):
    def wrapper(args, **kwargs):
        before = time()
        result = func(args, **kwargs)
        after = time()
        print("Cette opération a pris : {}".format(after - before))
        return result
    return wrapper