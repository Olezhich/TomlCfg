from typing import Any


def merge(main : dict[str, Any] | None, additional : dict[str, Any] | None) -> None:
    """recursively merges dicts"""
    for key, val in additional.items():
        if key in main.keys():
            if type(val) != type(main[key]):
                raise KeyError(f'type of main[{key}] != type of additional[{key}]')
            elif isinstance(val, dict):
                merge(main[key], val)
            else:
                main[key] = val
        else:
            main[key] = val