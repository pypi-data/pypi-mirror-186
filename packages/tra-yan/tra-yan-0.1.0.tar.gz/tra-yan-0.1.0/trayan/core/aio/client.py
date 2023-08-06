import os
from typing import Optional, Iterable

import aiofiles
from httpx import AsyncClient

from trayan.models.errors import SidParseError, BadResponse
from trayan.models.translator import Language
from trayan.utils import cached_property
from ..base import BaseTraYan


class AsyncTraYan(BaseTraYan):
    async def detect(self, text: str, hints: Optional[Iterable[str]] = None) -> 'Language':
        req = self._detect_request
        req.url = req.url.copy_merge_params(
            params=dict(
                sid=await self.sid,
                text=text,
            ) | (dict(hint=hints if isinstance(hints, str) else ','.join(hints)) if hints else {})
        )
        resp = await self._session.send(req)
        if resp.status_code == 200:
            return resp.json().get('lang')
        raise BadResponse(resp.content.decode('utf-8'))

    async def translate(
            self,
            text: str,
            source_language: str = Language.EN,
            target_language: str = Language.RU
    ) -> str:
        req = self._translate_request
        req.url = req.url.copy_merge_params(
            params=dict(
                id=await self.id,
                lang=f'{source_language}-{target_language}',
                text=text,
            )
        )
        resp = await self._session.send(req)
        if resp.status_code == 200:
            return resp.json().get('text')[0]
        raise BadResponse(resp.content.decode('utf-8'))

    async def __aenter__(self):
        await self.close()
        self.start()
        return self

    async def __aexit__(self, *err):
        await self.close()

    def _init_session(self, is_ssl: bool = True) -> AsyncClient:
        return AsyncClient(proxies=self._proxy)

    async def close(self) -> None:
        if self._session:
            await self._session.aclose()
            self._session = None

    @cached_property(ttl=60 * 60 * 24 * 4)
    async def sid(self) -> str:
        if not self._check_cache():
            sid = await self._gen_sid()
            try:
                await self._save_cache(sid)
            except PermissionError:
                ...
            return sid
        return await self._get_cache()

    @cached_property
    async def id(self) -> str:
        return f'{await self.sid}{self._suffix}'

    async def _save_cache(self, data: str) -> None:
        async with aiofiles.open(self._CACHE_PATH, 'w', encoding='utf8') as f:
            os.utime(self._CACHE_PATH, None)
            await f.write(data)

    async def _get_cache(self) -> Optional[str]:
        async with aiofiles.open(self._CACHE_PATH, 'r', encoding='utf8') as f:
            return await f.read()

    async def _gen_sid(self) -> str:
        resp = await self._session.send(self._get_sid_request)
        if sid := self._sid_reg_exp.findall(resp.content.decode('utf-8')):
            return '.'.join(i[::-1] for i in sid[0].split('.'))
        raise SidParseError()
