import os
import re
from abc import ABCMeta, abstractmethod
from base64 import b64decode
from random import randint
from time import time
from typing import Optional, Dict

from httpx import Request
from httpx._types import ProxiesTypes

from trayan.models.request import RequestMethod
from trayan.models.translator import ApiMethod


class BaseTraYan:
    __metaclass__ = ABCMeta

    BASE_SITE_URL = b64decode(b'aHR0cHM6Ly90cmFuc2xhdGUueWFuZGV4LnJ1Lw==').decode('utf-8')
    BASE_API_URL = b64decode(b'aHR0cHM6Ly90cmFuc2xhdGUueWFuZGV4Lm5ldC9hcGkvdjEvdHIuanNvbi8=').decode('utf-8')
    SUPPORTED_LANGS = {
        'az': 'Azerbaijani',
        'ml': 'Malayalam',
        'sq': 'Albanian',
        'mt': 'Maltese',
        'am': 'Amharic',
        'mk': 'Macedonian',
        'en': 'English',
        'mi': 'Maori',
        'ar': 'Arabic',
        'mr': 'Marathi',
        'hy': 'Armenian',
        'mhr': 'Mari',
        'af': 'Afrikaans',
        'mn': 'Mongolian',
        'eu': 'Basque',
        'de': 'German',
        'ba': 'Bashkir',
        'ne': 'Nepalese',
        'be': 'Belarusian',
        'no': 'Norwegian',
        'bn': 'Bengal',
        'pa': 'Punjabi',
        'my': 'Burmese',
        'pap': 'Papiamento',
        'bg': 'Bulgarian',
        'fa': 'Persian',
        'bs': 'Bosnian',
        'pl': 'Polish',
        'cy': 'Welsh',
        'pt': 'Portuguese',
        'hu': 'Hungarian',
        'ro': 'Romanian',
        'vi': 'Vietnamese',
        'ru': 'Russian',
        'ht': 'Haitian (Creole)',
        'ceb': 'Cebuano',
        'gl': 'Galician',
        'sr': 'Serbian',
        'nl': 'Dutch',
        'si': 'Sinhalese',
        'mrj': 'Hill Mari',
        'sk': 'Slovak',
        'el': 'Greek',
        'sl': 'Slovenian',
        'ka': 'Georgian',
        'sw': 'Swahili',
        'gu': 'Gujarati',
        'su': 'Sundanese',
        'da': 'Danish',
        'tg': 'Tajik',
        'he': 'Hebrew',
        'th': 'Thai',
        'yi': 'Yiddish',
        'tl': 'Tagalog',
        'id': 'Indonesian',
        'ta': 'Tamil',
        'ga': 'Irish',
        'tt': 'Tartar',
        'it': 'Italian',
        'te': 'Telugu',
        'is': 'Icelandic',
        'tr': 'Turkish',
        'es': 'Spanish',
        'udm': 'Udmurt',
        'kk': 'Kazakh',
        'uz': 'Uzbek',
        'kn': 'Kannada',
        'uk': 'Ukrainian',
        'ca': 'Catalan',
        'ur': 'Urdu',
        'ky': 'Kirghiz',
        'fi': 'Finnish',
        'zh': 'Chinese',
        'fr': 'French',
        'ko': 'Korean',
        'hi': 'Hindi',
        'xh': 'Xhosa',
        'hr': 'Croatian',
        'km': 'Khmer',
        'cs': 'Czech',
        'lo': 'Laotian',
        'sv': 'Swedish',
        'la': 'Latin',
        'gd': 'Scottish',
        'lv': 'Latvian',
        'et': 'Estonian',
        'lt': 'Lithuanian',
        'eo': 'Esperanto',
        'lb': 'Luxembourg',
        'jv': 'Javanese',
        'mg': 'Malagasy',
        'ja': 'Japanese',
        'ms': 'Malay'
    }

    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'
    _HEADERS = {
        'Host': 'translate.yandex.ru',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': USER_AGENT,
    }
    _API_HEADERS = {
        'Host': 'translate.yandex.net',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Origin': 'https://translate.yandex.ru',
        'Referer': 'https://translate.yandex.ru/',
        'User-Agent': USER_AGENT,
    }

    _SID_REG_EXP = r'SID\s?:\s?[\'"]([^\'"]+)[\'"]'

    SID_EXPIRES_TIME = 60 * 60 * 24 * 4

    _CACHE_PATH = os.path.join(os.path.expanduser('~'), '.trayan-old.key')

    def __init__(self, proxy: Optional[ProxiesTypes] = None):
        self._session = None
        self._proxy = proxy

        self._sid_reg_exp = re.compile(self._SID_REG_EXP)

        self._get_sid_request = Request(
            RequestMethod.GET,
            self.BASE_SITE_URL,
            headers=self._HEADERS,
        )
        self._detect_request = Request(
            RequestMethod.GET,
            f'{self.BASE_API_URL}{ApiMethod.DETECT}',
            headers=self._API_HEADERS,
            params=dict(
                srv='tr-text',
                options=1,
            ),
        )
        self._translate_request = Request(
            RequestMethod.POST,
            f'{self.BASE_API_URL}{ApiMethod.TRANSLATE}',
            headers=self._API_HEADERS,
            params=dict(
                srv='tr-text',
                reason='type-end',
                format='text',
                ajax=1,
                options=4,
            ),
        )

        self.start()

    def start(self) -> None:
        self._session = self._init_session()

    @abstractmethod
    def _init_session(self):
        raise NotImplementedError

    @abstractmethod
    def close(self):
        raise NotImplementedError

    @abstractmethod
    def detect(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def translate(self, *args, **kwargs):
        raise NotImplementedError

    @property
    def _suffix(self) -> str:
        return f'-{randint(0, 9)}-0'

    @classmethod
    @property
    def supported_langs(cls) -> Dict[str, str]:
        return cls.SUPPORTED_LANGS

    @classmethod
    def get_supported_langs(cls) -> Dict[str, str]:
        return cls.supported_langs

    def _check_cache(self) -> bool:
        if os.path.exists(self._CACHE_PATH):
            try:
                return os.path.isfile(self._CACHE_PATH) & \
                    ((time() - os.path.getmtime(self._CACHE_PATH)) < self.SID_EXPIRES_TIME)
            except PermissionError:
                ...
