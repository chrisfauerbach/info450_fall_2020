import logging
# create logger
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


def fib(n):
    first = 0
    second = 1
    for x in range(n):
        print(first)
        first, second = second, first+second

if __name__ == "__main__":
    logging.debug("Calling fib(3)")
    fib(3)
    logging.debug("Calling fib(8)")
    fib(8)
