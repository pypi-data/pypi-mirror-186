import logging
from skipi.function import FunctionFileLoader, Function

def get_logger(name):
    """
    Creates a logger with given name
    :param str name:
    :return: logging object
    """
    logger = logging.getLogger(name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


class UXDFileLoader(FunctionFileLoader):
    def from_file(self):
        from numpy import loadtxt
        q, dq, R, dR = loadtxt(self._file, usecols=(0, 1, 2, 3)).T

        f = Function.to_function(q, R)
        dx = Function.to_function(q, dq)
        dy = Function.to_function(q, dR)
        f.set_dy(dy)
        f.set_dx(dx)

        return f