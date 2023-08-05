import asyncio
import json
import os

from playwright.async_api import async_playwright

import scrapyish
from scrapyish.http import Response


class Crawler:
    def __init__(self, spiderclass=None, settings=None):
        self.settings = settings
        self.spiderclass = spiderclass
        self.crawling = False
        self.spider = None

    def crawl(self, spiderclass=None):
        asyncio.run(self._crawl(spiderclass=spiderclass))

    async def _crawl(self, spiderclass=None):
        if self.crawling:
            raise RuntimeError("Crawling is already taking place")
        self.crawling = True
        if self.spiderclass is not None:
            self.spider = self.spiderclass(self)
        elif spiderclass is not None:
            self.spider = spiderclass(self)
            self.spiderclass = spiderclass
        self.settings = self.spiderclass._default_settings
        self.settings.update(self.spiderclass.settings)
        self.outpath = self.spiderclass.settings["FEEDS_PATH"]
        async with async_playwright() as playwright:
            self.browser = await playwright.chromium.launch()
            await self.run_spider()
        self.crawling = False

    async def run_spider(self):
        requests = []
        async for request in self.spider.start_requests():
            requests.append(request)
        result = asyncio.gather(*[self.crawl_request(i) for i in requests])
        await result

    async def crawl_request(self, request):
        page = await self.browser.new_page()
        await page.goto(request.url)
        html = await page.content()
        response = Response(
            request.url,
            body=html,
            page=page,
            browser=self.browser,
            request=request,
        )
        callback = request._callback
        if request._callback is None:
            callback = self.spider.parse
        requests = []
        async for item in callback(response, **request.cb_kwargs):
            if isinstance(item, dict):
                if os.path.exists(self.outpath):
                    data = json.load(open(self.outpath, "rt"))
                    data.append(item)
                    json.dump(data, open(self.outpath, "wt"), indent=4)
                else:
                    data = [item]
                    json.dump(data, open(self.outpath, "wt"), indent=4)
            elif isinstance(item, scrapyish.Request):
                requests.append(item)
        result = asyncio.gather(*[self.crawl_request(i) for i in requests])
        await result
