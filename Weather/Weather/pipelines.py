# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymongo import MongoClient


class WeatherPipeline:
    def open_spider(self, spider):
        if spider.name == 'tianqi':
            self.myclient = MongoClient("mongodb://192.168.174.128:27017/")
            self.mydb = self.myclient["Weather"]
            if "weather" in self.mydb.list_collection_names():
                self.mydb.drop_collection("weather")
            self.mycol = self.mydb["weather"]

    def process_item(self, item, spider):
        if spider.name == 'tianqi':
            item = dict(item)
            self.mycol.insert_one(item)
            return item

    def close_spider(self, spider):
        if spider.name == 'tianqi':
            self.myclient.close()
