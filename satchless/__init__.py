"""
Satchless

An e-commerce framework for Python
"""
import logging
from . import process
from . import item
from . import cart

__all__ = ['cart', 'item', 'process']

class SatchlessBaseError(Exception):
    """Base Exception class

    :note: This will try to use the logging module
    :param message: the Exception message
    :type message: str

    :param data: Used to format the message string
    """
    def __init__(self, message, data=None):
        try:
            message = message % data
        except:
            pass

        # log the message using the class name
        logging.getLogger( self.__class__.__name__ ).exception( message )

        Exception.__init__(self, message)

class SatchlessBaseClass(object):
    """Base class used throughout satchless
    
    """
    ArgsError = SatchlessBaseError
    KwargsError = SatchlessBaseError
    ParamError = SatchlessBaseError

    LOG = None
        
    def logit(self, message, level=logging.DEBUG):
        """Write `message` to logging

        :param message: String to send
        :param level: Desired log level (Default: logging.DEBUG)
        :raises: satchless.SBase.ParamError
        """
        if not self.LOG:
            # use subclass name, not SBase
            self.LOG = getLogger( self.__class__.__name__ ) 

        try:
            getattr( self.LOG, level )(message)
        except:
            raise ParamError("could not find level (%s) in self.LOG" % level)

