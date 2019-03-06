import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://leblagueur.e-monsite.com/pages/proverbes-et-citations-loufoques.html']

    def parse(self, response):
        for title in response.css('div.rows p'):
            yield {'quote': title.css('p ::text').get()}