from pathlib import Path
from typing import Iterable

import scrapy
from scrapy import Request


class DevtoSpider(scrapy.Spider):
    name = 'devto_spider'

    css_selectors = {
        'title': '.fs-3xl::text',

    }

    def start_requests(self):
        urls = [
            'https://dev.to/glitch/what-is-worth-learning-41e3',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        if response.status == 200:
            title = response.css(self.css_selectors['title']).get().strip()
            print(title)
            self.log(f'page saved{response.url}')
