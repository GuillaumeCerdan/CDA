
def catchable(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print("Exception")
 
    return wrapper

# def catchable(func):
#     def wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except:
#             print("Exception")

#     return wrapper
