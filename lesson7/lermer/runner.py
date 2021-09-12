from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess

from lesson7.lermer import settings
from lesson7.lermer.spiders.lermerlin import LermerlinSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(crawler_settings)
    answer = input('Введите запрос для поиска: ')
    process.crawl(LermerlinSpider, query=answer)

    process.start()