import scrapy


class CssScrapperSpider(scrapy.Spider):
    name = "xpath-scraper-results"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'text': quote.xpath("//span[@class='text']/text()").get(),
                'author': quote.xpath("//small[@class='author']/text()").get(),
                'tags': quote.xpath("//div[@class='tags']//a[@class='tag']/text()").getall(),
            }

        next_page = response.xpath("//li[@class='next']/a").attrib["href"]
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
