"""Module to read and validate the given arguments.
"""
import os
import argparse

from typing import List
from pathlib import Path

_IMAGES_SUFFIX = ['.jpg', '.png', '.JPG', '.PNG']


def gen_arguments(argv: List[str]):
    """Reads arguments

    Args:
        argv (List[str]): The list of given argument.
    Returns:
        (argparse.ArgumentParser): The given arguments.
    Raises:
        SystemExit: Something goes wrong with input arguments.
    """

    _parser = argparse.ArgumentParser()

    _parser.add_argument(
        '-i',
        '--imagesDir',
        dest='images_dir',
        type=str,
        required=True,
        help='The local directory path includes images to be labeled.'
    )
    _parser.add_argument(
        '-o',
        '--Output',
        dest='output',
        type=str,
        required=True,
        help='The local directory path to save the labeled images.'
    )

    return _parser.parse_args(argv)


def does_input_dir_valid(
        local_images_path: str):
    """Validates the input directory path of images.

    Args:
        local_images_path (str): The given local path.
    Rteurns:
        None
    Raises:
        FileNotFoundError: When the given path does not exist.
        ValueError: When the given directory is empty.
    """
    if not os.path.isdir(local_images_path):
        raise FileNotFoundError('The given path does not refer to a directory with images content.')

    intrr = 0
    for suffix in _IMAGES_SUFFIX:
        images_names = list(Path(local_images_path).glob(f'*{suffix}'))
        if len(images_names) != 0:
            intrr += 1
        if len(images_names) == 0 and intrr == 0:
            raise ValueError(
                f'The given directory: "{local_images_path}" does not includes images.')
