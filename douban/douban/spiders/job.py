
import scrapy
# 导入建模
from douban.items import DoubanItem
from twisted.spread.pb import respond
class JobSpider(scrapy.Spider):
    name = "job"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    # 数据分析
    def parse(self, response, **kwargs):
        videoList = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for video in videoList:
            item = DoubanItem()
            item["videoName"] = video.xpath('./div/div[2]/div[1]/a/span/text()').extract_first()
            item["videoLink"] = video.xpath('./div/div[2]/div[1]/a/@href').extract_first()
            item["producer"] = video.xpath('./div/div[2]/div[2]/p[1]/text()').extract_first().strip()
            item["star"] = video.xpath('./div/div[2]/div[2]/div/span[2]/text()').extract_first()
            item["reviews"] = video.xpath('./div/div[2]/div[2]/div/span[4]/text()').extract_first()
            yield item
        # 翻页
        partUrl = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract_first()
        if partUrl != None:
            nextUrl = response.urljoin(partUrl)
            yield scrapy.Request(
                url=nextUrl,
                callback=self.parse
            )
