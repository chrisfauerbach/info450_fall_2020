import logging
# create logger
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

def hello_world(name=None):
    if not name:
        print("Hello, World!")
    else:
        print(f"Hello, {name}!")

if __name__ == "__main__":
    logging.debug("No parameters.")
    hello_world()
    logging.debug("Explicit None")
    hello_world(None)
    logging.debug("Chris")
    hello_world('Chris')
    logging.debug("name=\"Mom\"")
    hello_world(name='Mom')
