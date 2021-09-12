# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient
from urllib.parse import urlparse


class LermerPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.lermer

    def process_item(self, item, spider):
        item['options'] = dict(zip(item['property'], item['property_val']))
        del item['property']
        del item['property_val']
        collection = self.mongobase[spider.name]
        collection.insert_one(item)
        return item


class LermerPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [itm[1] for itm in results if itm[0]]
        return item

    def file_path(self, request, response=None, info=None, *, item=None):
        return f"{item['name']}/{os.path.basename(urlparse(request.url).path)}"
