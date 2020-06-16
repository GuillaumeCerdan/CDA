def catchableConnection(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print("Un problème est apparu avec la connexion...")
 
    return wrapper