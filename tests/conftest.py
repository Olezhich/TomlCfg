import pytest
from .dicts import *

@pytest.fixture()
def mock_files(monkeypatch):
    def mock_open(filename, *args, **kwargs):
        class MockFile:
            def __enter__(self):
                return self
            def __exit__(self, *args, **kwargs):
                pass
            def read(self):
                if filename == 'default_cfg.toml':
                    return default_cfg
                if filename == 'secret_cfg.toml':
                    return secret_cfg
                if filename == 'cfg_w_containers1.toml':
                    return cfg_w_containers1
                if filename == 'cfg_w_containers2.toml':
                    return cfg_w_containers2
                if filename == 'cfg_w_containers3.toml':
                    return cfg_w_containers3
                else:
                    raise FileNotFoundError
        return MockFile()
    monkeypatch.setattr('builtins.open', mock_open)

@pytest.fixture()
def first_case_merge():
    return first_case_dict

@pytest.fixture()
def second_case_merge():
    return second_case_dict