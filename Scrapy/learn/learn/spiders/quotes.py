import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_url = ['https://quotes.toscrape.com/']

    def parse(self, response):
        title = response.css('title').extract()
        yield {'title text': title}
