import scrapy
from scrapy.http import HtmlResponse
from lesson7.lermer.items import LermerItem
from scrapy.loader import ItemLoader

class LermerlinSpider(scrapy.Spider):
    name = 'lermerlin'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, query, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f'https://leroymerlin.ru/search/?q={query}']

    def parse(self, response: HtmlResponse, **kwargs):
        links = response.xpath("//a[@data-qa='product-name']")
        next_page = response.xpath('//a[@ data-qa-pagination-item="right"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        for link in links:
            yield response.follow(link, callback=self.parse_dv)

    def parse_dv(self, response:HtmlResponse):
        loader = ItemLoader(item=LermerItem(), response=response)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('price', "//span[@slot='price']/text()")
        loader.add_xpath('photos', "//img[@alt='product image']/@src")
        loader.add_xpath('property', "//dt[@class='def-list__term']/text()")
        loader.add_xpath('property_val', "//dd[@class='def-list__definition']/text()")
        loader.add_value('options','')
        loader.add_value('url', response.url)
        yield loader.load_item()
        
