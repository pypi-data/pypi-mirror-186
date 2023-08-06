from typing import Optional, Iterable

from trayan.models.translator import Language
from .client import AsyncTraYan


async def async_detect(
        text: str,
        hints: Optional[Iterable[str]] = None,
        proxy: Optional[Iterable[str]] = None,
) -> 'Language':
    async with AsyncTraYan(proxy=proxy) as t:
        return await t.detect(text=text, hints=hints)


async def async_translate(
        text: str,
        source_language: str = Language.EN,
        target_language: str = Language.RU,
        proxy: Optional[Iterable[str]] = None,
) -> str:
    async with AsyncTraYan(proxy=proxy) as t:
        return await t.translate(text=text, source_language=source_language, target_language=target_language)
