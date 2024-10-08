import scrapy
from scrapy_splash import SplashRequest  # 使用scrapy_splash包提供的request对象


class WithSplashSpider(scrapy.Spider):
    name = 'with_splash'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=13161933309']

    def start_requests(self):
        yield SplashRequest(self.start_urls[0],
                            callback=self.parse_splash,
                            args={'wait': 10},  # 最大超时时间，单位：秒
                            endpoint='render.html',
                            dont_filter=True)  # 使用splash服务的固定参数

    def parse_splash(self, response):
        print("==========================================")
        print(response.body)
