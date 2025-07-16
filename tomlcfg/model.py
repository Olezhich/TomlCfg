from typing import Any
from merge import merge
import toml

class BaseModel:
    def __init__(self, *config_paths : str | None) -> None:
        """configs will be merged in the following order: arg0 <- arg1 <- arg2 ..."""
        self._config : dict[str, Any] | None = None
        for arg in config_paths:
            with open(arg, 'r') as f:
                current_cfg = toml.load(f)
                self._config = merge(self._config, current_cfg)
