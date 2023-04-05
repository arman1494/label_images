import os
import pytest
from src.args_parser import does_input_dir_valid


def test_does_input_dir_valid_exist():
    """When the input directory exist and is non-empty
    """
    test_path = os.path.join('tests', 'test_data')
    does_input_dir_valid(local_images_path=test_path)


def test_does_input_dir_valid_non_inexistence():
    """When the input directory does not exist
    """
    test_path = 'dummy_path'
    with pytest.raises(FileNotFoundError) as exp:
        does_input_dir_valid(local_images_path=test_path)
    assert exp.type == FileNotFoundError
    assert str(exp.value) == 'The given path does not refer to a directory with images content.'


def test_does_input_dir_valid_empty(mocker):
    """When the input directory exist but empty.
    """
    test_path = 'dummy_path'
    mocked_os_path = mocker.patch('os.path.isdir', return_value=True)
    with pytest.raises(ValueError) as exp:
        does_input_dir_valid(local_images_path=test_path)
    assert exp.type == ValueError
    assert str(exp.value) == f'The given directory: "{test_path}" does not includes images.'
    mocked_os_path.assert_called_once_with(test_path)
