""" wg-federation """
import sys
from wg_federation.main import Main
from wg_federation.constants import __version__


def main():
    """ Main """
    Main().main()


if __name__ == '__main__':
    sys.exit(main())
