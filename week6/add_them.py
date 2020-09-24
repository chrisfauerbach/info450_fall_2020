import logging
# create logger
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

def add_them(first, second):
    return first + second

if __name__ == "__main__":
    logging.debug("add_them(1, 2)")
    logging.debug(add_them(1, 2))
    logging.debug("add_them(3, 4)")
    logging.debug(add_them(3, 4))
    logging.debug("add_them(\"dog\", \"type\")")
    logging.debug(add_them("dog", "type"))
