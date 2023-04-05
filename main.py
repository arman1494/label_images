"""Main module to run the tool.
"""

import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'src'))

from src.args_parser import (gen_arguments,
                             does_input_dir_valid)  # NOQA


def main(argv: list = None):
    """Main function to run the script.

    Args:
        argv (list, optional): The input arguments. Defaults to None.
    Returns:
        None
    Raises:
        Exception: Something goes wrong with given arguments.
    """


if __name__ == '__main__':
    try:
        main()
    except Exception as exp:
        sys.exit(exp)
