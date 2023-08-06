import os
from typing import Optional, Iterable

from httpx import Client

from trayan.models.errors import SidParseError, BadResponse
from trayan.models.translator import Language
from trayan.utils import cached_property
from ..base import BaseTraYan


class TraYan(BaseTraYan):
    def detect(self, text: str, hints: Optional[Iterable[str]] = None) -> 'Language':
        req = self._detect_request
        req.url = req.url.copy_merge_params(
            params=dict(
                sid=self.sid,
                text=text,
            ) | (dict(hint=hints if isinstance(hints, str) else ','.join(hints)) if hints else {})
        )
        resp = self._session.send(req)
        if resp.status_code == 200:
            return resp.json().get('lang')
        raise BadResponse(resp.content.decode('utf-8'))

    def translate(
            self,
            text: str,
            source_language: str = Language.EN,
            target_language: str = Language.RU
    ) -> str:
        req = self._translate_request
        req.url = req.url.copy_merge_params(
            params=dict(
                id=self.id,
                lang=f'{source_language}-{target_language}',
                text=text,
            )
        )
        resp = self._session.send(req)
        if resp.status_code == 200:
            return resp.json().get('text')[0]
        raise BadResponse(resp.content.decode('utf-8'))

    def __enter__(self):
        self.close()
        self.start()
        return self

    def __exit__(self, *err):
        self.close()

    def _init_session(self, is_ssl: bool = True) -> Client:
        return Client(proxies=self._proxy)

    def close(self) -> None:
        if self._session:
            self._session.close()
        self._session = None

    @cached_property(ttl=60 * 60 * 24 * 4)
    def sid(self) -> str:
        if not self._check_cache():
            sid = self._gen_sid()
            try:
                self._save_cache(sid)
            except PermissionError:
                ...
            return sid
        return self._get_cache()

    @cached_property
    def id(self) -> str:
        return f'{self.sid}{self._suffix}'

    def _save_cache(self, data: str) -> None:
        with open(self._CACHE_PATH, 'w', encoding='utf8') as f:
            os.utime(self._CACHE_PATH, None)
            f.write(data)

    def _get_cache(self) -> Optional[str]:
        with open(self._CACHE_PATH, 'r', encoding='utf8') as f:
            return f.read()

    def _gen_sid(self) -> str:
        resp = self._session.send(self._get_sid_request)
        if sid := self._sid_reg_exp.findall(resp.content.decode('utf-8')):
            return '.'.join(i[::-1] for i in sid[0].split('.'))
        raise SidParseError()
