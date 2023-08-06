
def logger(func):
    import logging
    logging.info(func.__name__)

    def wrapper(*args, **kwargs):
        logging.info(f'args: {args}, kwargs{kwargs}')
        return func(*args, **kwargs)

    return wrapper


def timer(func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'Time {func.__name__} ... {t2:.2f} sec')
        return res

    return wrapper

### How to use it?
#import time
# @timer
# def myfunc(a):
#     time.sleep(1)
#     return a * a

