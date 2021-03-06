# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Movie(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    year = scrapy.Field()
    description = scrapy.Field()
    cast = scrapy.Field()
    characters = scrapy.Field()
    director = scrapy.Field()
    avg_rating = scrapy.Field()
    watches = scrapy.Field()
    likes = scrapy.Field()
    url = scrapy.Field()
    time = scrapy.Field()
