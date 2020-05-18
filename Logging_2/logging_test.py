import logging

# Root logger(This full paragraph have to be defined for us to use the variable roo_logger in log statments)
# root_logger = logging.getLogger()
# root_logger.setLevel(logging.DEBUG)
# sh = logging.StreamHandler()
# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# sh.setFormatter(formatter)
# root_logger.addHandler(sh)

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

# Application logger
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.propagate = False



def add(x, y):
    return x+y

def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

x = 10
y = 2

add_val = add(x, y)
logger.debug(f"{add_val}")
root_logger.debug(f"This is from the root : {add_val}")
logging.debug(f"This is from the root with simple logging: {add_val}")

sub_val = subtract(x, y)
logger.debug(f"{sub_val}")
root_logger.debug(f"This is from the root : {sub_val}")
logging.debug(f"This is from the root with simple logging: {sub_val}")

mul_val = multiply(x, y)
logger.debug(f"{mul_val}")
root_logger.debug(f"This is from the root : {mul_val}")
logging.debug(f"This is from the root with simple logging: {mul_val}")

div_val = divide(x, y)
logger.debug(f"{div_val}")
root_logger.debug(f"This is from the root : {div_val}")
logging.debug(f"This is from the root with simple logging: {div_val}")
