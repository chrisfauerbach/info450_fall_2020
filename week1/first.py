import logging
import json

# create logger
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

def printThingAsJSON(thing):
    print(json.dumps(thing))

if __name__ == "__main__":
    output = {"Hi": "Mom"}
    printThingAsJSON(output)
    logging.debug("Completed.")

