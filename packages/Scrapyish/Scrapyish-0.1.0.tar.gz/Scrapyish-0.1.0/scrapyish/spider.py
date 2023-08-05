"""
Spider base class was mostly copied from the original scrapy project.
More information can be found https://github.com/scrapy/scrapy.
"""
from scrapyish.http import Request


class Spider:
    """
    Base class for scrapyish spiders.
    """

    name: str
    _default_settings = {
        "FEEDS_PATH": "items.json",
        "CONCURRENT_REQUESTS": 30,
        "DOWNLOAD_DELAY": 0,
    }
    settings = {}

    def __init__(self, crawler, name=None):
        self.crawler = crawler
        if name is not None:
            self.name = name
        if not hasattr(self, "start_urls"):
            self.start_urls = []

    async def start_requests(self):
        if not self.start_urls and hasattr(self, "start_url"):
            raise AttributeError(
                "Crawling could not start: 'start_urls' not found "
                "or empty (but found 'start_url' attribute instead, "
                "did you miss an 's'?)"
            )
        for url in self.start_urls:
            yield Request(url)

    async def parse(self, response, **kwargs):
        raise NotImplementedError(
            f"{self.__class__.__name__}.parse callback {response}{kwargs}"
        )

    def __repr__(self):
        return f"<{type(self).__name__} {self.name!r} at 0x{id(self):0x}>"
