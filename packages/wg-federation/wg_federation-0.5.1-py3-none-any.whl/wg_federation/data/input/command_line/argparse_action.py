from enum import Enum


class ArgparseAction(str, Enum):
    """ Enum of all possible actions for argparse options/arguments """

    APPEND_CONST = 'append_const'
    COUNT = 'count'
    EXTEND = 'extend'
    HELP = 'help'
    STORE = 'store'
    STORE_CONST = 'store_const'
    STORE_FALSE = 'store_false'
    STORE_TRUE = 'store_true'
    VERSION = 'version'
