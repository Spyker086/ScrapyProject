# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst


def get_price(value):
    value = float(value.replace(' ',''))
    return value

def get_pv(value):
    value = value.lstrip().rstrip()
    return value

class LermerItem(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field(input_processor=MapCompose(get_price), output_processor=TakeFirst())
    property = scrapy.Field()
    property_val = scrapy.Field(input_processor=MapCompose(get_pv))
    options = scrapy.Field()
    _id = scrapy.Field()

