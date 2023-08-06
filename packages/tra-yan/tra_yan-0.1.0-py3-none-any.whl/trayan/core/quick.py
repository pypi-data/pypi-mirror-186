from typing import Dict

from .sync import TraYan


def get_supported_langs() -> Dict[str, str]:
    return TraYan.get_supported_langs()
