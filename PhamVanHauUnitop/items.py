# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PhamvanhauunitopItem(scrapy.Item):
    courseURL = scrapy.Field()
    votenumber = scrapy.Field()
    rating = scrapy.Field()
    newfee = scrapy.Field()
    oldfee = scrapy.Field()
    lessonnum = scrapy.Field()