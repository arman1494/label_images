"""Module to do local operations.
"""
import sys
import os

from typing import List
from pathlib import Path

sys.path.append(os.path.join(os.getcwd(), 'src'))

from args_parser import IMAGES_SUFFIX  # NOQA


def read_dir(
        local_dir_path: str) -> List[str]:
    """Functions to read the images from the local directory.

    Args:
        local_dir_path (str): Path to the directory which includes the images.
    Retruns:
        images_paths(List[str]): List of images paths.
    Raises:
        None
    """
    images_paths = []
    for suffix in IMAGES_SUFFIX:
        images_names = list(Path(local_dir_path).glob(f'*{suffix}'))
        path = [str(Path(local_dir_path)/name) for name in images_names]
        images_paths.extend(path)
    return images_paths


def gen_output_dir(
        local_output_path: str) -> str:
    """Generate output directory.

    Args:
        local_output_path (str): Path to create output directory.
    Returns:
        (str): The output path.
    Raises:
        None
    """
    tmp_output_path = Path(local_output_path)
    tmp_output_path.mkdir(parents=True, exist_ok=True)

    return str(tmp_output_path)
