from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess

from lesson6.libparser import settings
from lesson6.libparser.spiders.labirint import LabirintSpider
from lesson6.libparser.spiders.book24 import Book24Spider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(crawler_settings)
    process.crawl(LabirintSpider)
    process.crawl(Book24Spider)

    process.start()