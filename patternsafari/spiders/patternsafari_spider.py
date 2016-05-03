from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy_splash import SplashRequest
from scrapy_splash import SplashMiddleware
from patternsafari.items import PatternsafariItem

class PatternsafariSpider(BaseSpider):
    name = "patternsafari"
    allowed_domains = ["http://patternsafari.91app.com"]
    start_urls = [
        "http://patternsafari.91app.com/v2/official/SalePageCategory/87757",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/87759",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/87720",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/78636",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/87862",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/90266",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/75427",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/84128",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/84129",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/84130",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/90993",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/72968",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/74791",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/83977",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/83975",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/85231",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/84160",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/87610",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/74792",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/78637",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/85230",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/78638",
        # "http://patternsafari.91app.com/v2/official/SalePageCategory/87566"
    ]
    def start_request(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 5.5}}
                })

    def parse(self, response):
        self.logger.info(response)
        sel = Selector(response)
        test = sel.xpath('//a/@href').extract()
        open("response", 'wb').write(response.body)


    # def parse_item(self, response):
    #     sel = Selector(response)
    #     items = []
    #     item = PatternsafariItem()
    #     item['productName'] = sel.xpath('//*[@id="salePageV2"]/div[1]/text()').extract()
    #     item['price'] = sel.xpath('//*[@id="salePageV2"]/div[2]/meta[2]/@content').extract()
    #     item['imgUrl'] = sel.xpath('//*[@id="carousel-example-generic"]/a[1]/div/div[1]/img/@src').re('\/\/(.+)')
    #     item['desc'] = sel.xpath('//*[@id="salePageV2"]/div[7]/ul/li/text()').extract()
    #     item['spec'] = sel.xpath('//*[@id="ppinfo"]/div[3]/table/tbody/tr/td/text()').extract()
    #     items.append(item)
    #     return items


        
        
