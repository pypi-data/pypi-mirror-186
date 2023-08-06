# tra-yan
awesome free asynchronous translator for python

## Installation
`pip install -U tra-yan`

## Usage
```python
async def use():
    from trayan import (
        TraYan, AsyncTraYan,
        detect, translate,
        async_detect, async_translate,
        get_supported_langs
    )
    from trayan.models.translator import Language

    ru = 'красивый мужчина в отличных трусах'
    en = 'a handsome man in great underpants'
    proxy = None  # 'scheme://login:password@ip:port'

    with TraYan() as t:
        print(f'{ru} — {t.detect(ru, Language.RU)}')
        print(f'ru-en — {t.translate(ru, Language.RU, Language.EN)}')

    print(f'{en} — {detect(en)}')
    print(f'en-ru — {translate(en)}')

    async with AsyncTraYan(proxy=proxy) as t:
        print(f'{en} — {await t.detect(en, (Language.RU,))}')
        print(f'en-ru — {await t.translate(en, Language.EN, Language.RU)}')

    print(f'{ru} — {await async_detect(ru, proxy=proxy)}')
    print(f'ru-en — {await async_translate(ru, proxy=proxy)}')

    print(f'поддерживаемые языки: {TraYan.supported_langs}')

    print(f'supported langs: {get_supported_langs()}')


if __name__ == '__main__':
    import asyncio

    asyncio.run(use())
```
