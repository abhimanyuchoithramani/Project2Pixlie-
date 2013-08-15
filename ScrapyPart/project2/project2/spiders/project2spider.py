from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from project2.items import Project2Item
#import MySQLdb
from scrapy.http import Request

class ProjectSpider(BaseSpider):
    name = "project2spider"
    allowed_domains = ["http://directory.thesun.co.uk/"]
    current_page_no = 1
    start_urls = [
        'http://directory.thesun.co.uk/find/uk/computer-repair'
        ]

    def get_next_url(self, fired_url):
        if '/page/' in fired_url:
            url, page_no = fired_url.rsplit('/page/', 1)
        else:
            if self.current_page_no != 1:
                #end of scroll
                return 
        self.current_page_no += 1
        return "http://directory.thesun.co.uk/find/uk/computer-repair/page/%s" % self.current_page_no


    
    
    

    
# the parse procedure, and here is the codes which declares which field to scrap. 
    def parse(self, response):
        fired_url = response.url
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@class="abTbl "] | //div[@class="icListItem"]')
        #items = []
        for site in sites:
            item = Project2Item()
            item['Catogory'] = site.select('span[@class="icListBusType"]/text()').extract()
            item['Bussiness_name'] = site.select('a/@title').extract()
            item['Description'] = site.select('span[last()]/text()').extract()
            item['Number'] = site.select('span[@class="searchInfoLabel"]/span/@id').extract()
            item['Web_url'] = site.select('span[@class="searchInfoLabel"]/a/@href').extract()
            item['adress_name'] = site.select('span[@class="searchInfoLabel"]/span/text()').extract()
            item['Photo_name'] = site.select('img/@alt').extract()
            item['Photo_path'] = site.select('img/@src').extract()
            #items.append(item)
            yield item
        next_url = self.get_next_url(fired_url)
        if next_url:
            yield Request(next_url, self.parse, dont_filter=True)
        #return items

 
