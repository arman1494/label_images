"""Main module to run the tool.
"""

import sys
import os

from typing import Tuple, List

sys.path.append(os.path.join(os.getcwd(), 'src'))

from args_parser import (gen_arguments,
                        does_input_dir_valid)  # NOQA
from utils import (gen_output_dir,
                   read_dir)  # NOQA


def main(argv: list = None) -> Tuple[List[str], str]:
    """Main function to run the script.

    Args:
        argv (list, optional): The input arguments. Defaults to None.
    Returns:
        (([str], str)): The paths to the images, and output dir
    Raises:
        Exception: Something goes wrong with given arguments.
    """
    given_args = gen_arguments(argv)

    does_input_dir_valid(local_images_path=given_args.images_dir)

    images = read_dir(local_dir_path=given_args.images_dir)
    output_path = gen_output_dir(local_output_path=given_args.output)
    return images, output_path


if __name__ == '__main__':
    try:
        main()
    except Exception as exp:
        sys.exit(exp)
