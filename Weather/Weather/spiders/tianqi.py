import scrapy

from Weather.items import WeatherItem
from scrapy.utils.iterators import xmliter


class TianqiSpider(scrapy.Spider):
    name = "tianqi"
    allowed_domains = ["nmc.cn"]
    start_urls = ["http://www.nmc.cn/publish/forecast.html"]

    def parse(self, response):
        list = response.xpath('/html/body/div[2]/div[4]/div//div/a')
        temp = WeatherItem()
        for node in list:
            temp = WeatherItem()
            temp['city'] = node.xpath('./div/div[1]/text()').extract_first()
            temp['cityLink'] = response.urljoin(node.xpath('./@href').extract_first())
            yield scrapy.Request(
                url=temp['cityLink'],
                callback=self.parse_day,
                meta={'weather': temp}
            )

    def parse_day(self, response):
        temp = response.meta['weather']
        day = response.xpath('//*[@id="day7"]/div[1]')
        temp['dayTemperature'] = day.xpath('./div/div[6]/text()').extract_first()
        temp['nightTemperature'] = day.xpath('./div/div[7]/text()').extract_first()
        temp['dayWeather'] = day.xpath('./div/div[3]/text()').extract_first()
        temp['nightWeather'] = day.xpath('./div/div[9]/text()').extract_first()
        yield temp
