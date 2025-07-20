import pytest

import tomlcfg


def test_merge_simple_cfgs(mock_files, first_case_merge):
    app = tomlcfg.BaseModel('default_cfg.toml', 'secret_cfg.toml')
    assert app._config == first_case_merge, 'simple case: 2 dicts, no containers'

def test_merge_complex_cfgs(mock_files, second_case_merge):
    app = tomlcfg.BaseModel('cfg_w_containers1.toml', 'cfg_w_containers2.toml')
    assert app._config == second_case_merge, 'complex case: 2 dicts with containers'

def test_key_error(mock_files):
    with pytest.raises(KeyError):
        app = tomlcfg.BaseModel('cfg_w_containers1.toml', 'cfg_w_containers3.toml')