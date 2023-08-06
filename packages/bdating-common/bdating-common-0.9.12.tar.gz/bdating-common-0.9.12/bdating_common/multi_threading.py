import threading
from functools import wraps
def threaded(f):
    ''' This decorator executes a function in a Thread'''
    @wraps(f)
    def wrapper(*args, **kwargs):
        thr = threading.Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper

