import asyncio
from playwright.async_api import async_playwright
from scrapyish.response import HTMLResponse

class Crawler:

    def __init__(self, spiderclass, settings=None):
        self.settings = settings
        self.spiderclass = spiderclass
        self.crawling = False
        self.spider = None

    async def crawl(self):
        if self.crawling:
            raise RuntimeError("Crawling is already taking place")
        self.crawling = True
        self.spider = self.spiderclass(self)
        async with async_playwright() as playwright:
            self.browser = await playwright.chromium.launch()
            await self.run_spider()

    async def run_spider(self):
        requests = []
        async for request in self.spider.start_requests():
            requests.append(request)
        await asyncio.gather(*[self.crawl_request(request) for request in requests])

    async def crawl_request(self, request):
        page = await self.browser.new_page()
        await page.goto(request.url)
        html = await page.content()
        response = HTMLResponse(request.url, body=html, encoding='utf8', page=page, browser=self.browser, request=request)
        callback = request._callback
        if request._callback is None:
            callback = self.spider.parse
        async for i in callback(response, **request.cb_kwargs):
            print(i)
