# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    cityLink = scrapy.Field()
    dayTemperature = scrapy.Field()
    nightTemperature = scrapy.Field()
    dayWeather = scrapy.Field()
    nightWeather = scrapy.Field()
