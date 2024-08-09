import aiohttp
from aiohttp import ClientTimeout
from bs4 import BeautifulSoup

import config


async def parse() -> dict:
    async with aiohttp.ClientSession(timeout=ClientTimeout(total=5)) as session:
        async with session.get(config.table_page_url) as resp:
            s = await resp.text()

    print('A')

    html = BeautifulSoup(s, features='lxml')
    rows = html.find_all('tr')

    res = {}

    for el in rows:
        html_name = el.find('td', attrs={'class': 'name'})
        if html_name is None:
            continue
        name = html_name.text[5:]
        res.update({name: []})

        for record in el.find_all('td', attrs={'class': 'verdict'}):
            if record['class'][1] in ['WA', 'NO']:
                continue

            res[name].append((record['title'][5:], record['class'][1]))

    return res
