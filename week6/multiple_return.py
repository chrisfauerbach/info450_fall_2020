import logging
# create logger
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

def return_multiple():
    return 1, 2, 3 

if __name__ == "__main__":
    logging.debug("All: ")
    a, b, c = return_multiple()
    logging.debug(a)
    logging.debug(b)
    logging.debug(c)
 
    logging.debug("only first")
    x, _, _ = return_multiple()
    logging.debug(x)

    logging.debug("what it does")
    d = return_multiple()
    logging.debug(d)
