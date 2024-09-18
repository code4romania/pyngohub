from datetime import datetime
from typing import Any, Dict


def extract_key(data: Dict[str, Any], key: str, *back_up_keys: str) -> Any:
    try:
        return data[key]
    except KeyError:
        if not back_up_keys:
            return None

    for back_up in back_up_keys:
        try:
            return data[back_up]
        except KeyError:
            continue

    return None


def convert_date(date: str) -> datetime:
    return datetime.fromisoformat(date)
