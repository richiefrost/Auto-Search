# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KslAutoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    make = scrapy.Field()
    model = scrapy.Field()
    year = scrapy.Field()
    mileage = scrapy.Field()
    price = scrapy.Field()
    vin = scrapy.Field()
    title_type = scrapy.Field()
    pass
