import logging
# create logger
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

def return_none():
    return None

def empty_return():
    return

if __name__ == "__main__":
    a = return_none()
    logging.debug(a)
    b = empty_return()
    logging.debug(b)
