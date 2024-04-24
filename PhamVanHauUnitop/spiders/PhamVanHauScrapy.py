import scrapy
from PhamVanHauUnitop.items import PhamvanhauunitopItem

class PhamvanhauscrapySpider(scrapy.Spider):
    name = "PhamVanHauScrapy"
    allowed_domains = ["unitop.vn"]
    start_urls = ["https://unitop.vn/"]

    def parse_start(self):
        yield scrapy.Request(url = start_urls, callback = self.parse)

    def parse(self, response):
        courseList = response.xpath('//div[@class="box-body"]/ul/li/div/a/@href').getall()
        for courseItem in courseList:
           item = PhamvanhauunitopItem()
           item['courseURL'] = response.urljoin(courseItem)
           request = scrapy.Request(url = response.urljoin(courseItem), callback = self.parseCourseDetail)
           request.meta['datacourse'] = item
           yield request
    def parseCourseDetail(self, response):
        item = response.meta['datacourse']
        item['votenumber'] = response.xpath('normalize-space(//span[@class="num-vote"]/text())').get()
        html_content = response.xpath('//div[@class="show-star"]').get()
        star_count = html_content.count('<i class="fas fa-star">')
        item['rating'] = star_count
        item['newfee'] = response.xpath('normalize-space(//span[@class="new-fee"]/text())').get()
        item['oldfee'] = response.xpath('normalize-space(//span[@class="old-fee"]/text())').get()
        item['lessonnum'] = response.xpath('normalize-space(//ul[@id="course-includes"]/li/text())').get()
        yield item

