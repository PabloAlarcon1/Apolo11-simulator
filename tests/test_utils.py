from src.utils import Utils
from pathlib import Path
from typing import Dict
import yaml
import pytest

class TestReadYaml:
    '''
    Class to test read_yaml method from Utils class.
    This method has 3 possible ouput:
    * Yaml file successfully read.
    * YAMLError: Corrupt yaml file exception
    * Exception: Unknown error, probably due to the fact the file does not exist.
    '''

    def test_valid_reading(self, test_data_path: Path):
        '''
        Test to validate that any valid yaml file can be successfully read
        '''
        path: Path = test_data_path.joinpath('good.yaml')
        content = Utils.read_yaml(path)
        assert isinstance(content, Dict)

    def test_yaml_error_exception(self, test_data_path: Path):
        '''
        Test to raise a YAMLError exception using an invalid yaml file
        '''
        with pytest.raises(yaml.YAMLError):
            path: Path = test_data_path.joinpath('corrupt.yaml')
            Utils.read_yaml(path)

    def test_general_exception(self):
        '''
        Test to raise a traditional Exception with an unexisting yaml file
        '''
        with pytest.raises(Exception):
            Utils.read_yaml('unexistent.yaml')