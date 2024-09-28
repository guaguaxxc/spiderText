# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 电影名
    videoName = scrapy.Field()
    # 电影链接
    videoLink = scrapy.Field()
    # 电影制作人名单
    producer = scrapy.Field()
    # 电影星级评分
    star = scrapy.Field()
    # 电影评价数量
    reviews = scrapy.Field()
    # 电影介绍
    introduce = scrapy.Field()
