import logging

# create logger
module_logger = logging.getLogger('spam_application.auxiliary')
#module_logger = logging.getLogger('something_else')

class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger('spam_application.auxiliary.Auxiliary')
        self.logger.info('creating an instance of Auxiliary from inside Auxillary class init')

    def do_something(self):
        self.logger.info('doing something inside Auxillary class')
        a = 1 + 1
        self.logger.info('done doing something inside Auxillary class')

def some_function():
    module_logger.info('received a call to "some_function"')
