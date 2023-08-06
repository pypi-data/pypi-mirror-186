from typing import Optional, Iterable

from .client import TraYan
from trayan.models.translator import Language


def detect(
        text: str,
        hints: Optional[Iterable[str]] = None,
        proxy: Optional[Iterable[str]] = None,
) -> 'Language':
    with TraYan(proxy=proxy) as t:
        return t.detect(text=text, hints=hints)


def translate(
        text: str,
        source_language: str = Language.EN,
        target_language: str = Language.RU,
        proxy: Optional[Iterable[str]] = None,
) -> str:
    with TraYan(proxy=proxy) as t:
        return t.translate(text=text, source_language=source_language, target_language=target_language)
