import scrapy

from ..utils import remove_html_tags, save_doc_id, is_exist, save_doc_body


class DevtoSpider(scrapy.Spider):
    name = 'devto_spider'
    css_selectors = {
        'doc_id': '#article-show-container::attr(data-article-id)',
        'title': '.fs-3xl::text',
        'author': 'a.fw-bold::text',
        'tags': "a.crayons-tag::text",
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
                try:
                    title = response.css(self.css_selectors['title']).get().strip()
                    author = response.css(self.css_selectors['author']).get().strip()
                    tags = response.css(self.css_selectors['tags']).getall()
                    publish_date = response.css(self.css_selectors['publish_date']).get().split('T')[0]
                    save_doc_id(doc_id=doc_id)
                    save_doc_body(response, self.css_selectors['article_body'], doc_id=doc_id, title=title,
                                  author=author,
                                  tags=tags, publish_date=publish_date)
                except Exception as e:
                    print(e)
                next_pages = response.css('a.mt-6::attr(href)').getall()
                for next_page in next_pages:
                    yield response.follow(next_page, callback=self.parse)
            else:
                pass
