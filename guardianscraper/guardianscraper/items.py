# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OpinionItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    byline = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()
    text = scrapy.Field()

