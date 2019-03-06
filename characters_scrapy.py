class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Personnage_d%27animationm']

    def parse(self, response):
        for title in response.css('div#mw-pages li'):
            yield {'character': title.css('a ::text').extract_first()}