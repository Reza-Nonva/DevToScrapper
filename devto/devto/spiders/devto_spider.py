import scrapy

from ..utils import remove_html_tags, write_data, is_exist, write_document


class DevtoSpider(scrapy.Spider):
    name = 'devto_spider'
    css_selectors = {
        'doc_id': '#article-show-container::attr(data-article-id)',
        'title': '.fs-3xl::text',
        'author': 'a.fw-bold::text',
        'publish_date': '.date-no-year::attr(datetime)',
        'article_body': '#article-body',
        'read_next': "a.mt-6::attr(href)",
    }

    def start_requests(self):
        urls = [
            'https://dev.to/glitch/what-is-worth-learning-41e3',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == 200:
            doc_id = response.css(self.css_selectors['doc_id']).get()

            if not is_exist(doc_id):
                title = response.css(self.css_selectors['title']).get().strip()
                author = response.css(self.css_selectors['author']).get().strip()
                publish_date = response.css(self.css_selectors['publish_date']).get().split('T')[0]
                write_data(doc_id=doc_id, title=title, author=author, publish_date=publish_date)
                write_document(response, doc_id, self.css_selectors['article_body'])

                next_pages = response.css('a.mt-6::attr(href)').getall()
                for next_page in next_pages:
                    yield response.follow(next_page, callback=self.parse)
            else:
                pass
