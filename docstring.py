import logging

logging.basicConfig(filename='purp.log', level=logging.INFO)

def does_something(arg):
    """yeet
"""
    if arg:
        print(arg)
        logging.info("yasss")
        logging.warn("red alert")
    else:
        print('not {}'.format(arg))
        logging.info("nop")
        logging.debug("cryptonite")
        logging.critical("hola como estas")

does_something(0)
        
