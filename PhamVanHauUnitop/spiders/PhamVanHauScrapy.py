import scrapy


class PhamvanhauscrapySpider(scrapy.Spider):
    name = "PhamVanHauScrapy"
    allowed_domains = ["unitop.vn"]
    start_urls = ["https://unitop.vn/"]

    def parse(self, response):
        courseList = response.xpath('//div[@class="box-body"]/ul/li/div/a/@href').getall()
        for courseItem in courseList:
            yield{
                "courseURL": courseItem
            }
