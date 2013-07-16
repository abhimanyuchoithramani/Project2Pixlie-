from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from project2.items import Project2Item
#import MySQLdb

class ProjectSpider(BaseSpider):
    name = "project2spider"
    allowed_domains = ["http://directory.thesun.co.uk/"]


    
    # ""**** I tried the below code to crawl pages also , BUT I was not sure abt it, so I used the hardcore values for all the pages***""


    #start_urls = [
     #   "http://directory.thesun.co.uk/find/uk/computer-repair"
    #]
    #next_urls = ['http://directory.thesun.co.uk/find/uk/computer-repair/page/%s' % page for page in xrange(2, 11)]
    #start_urls.extend(next_urls)
     
    start_urls = [
        'http://directory.thesun.co.uk/find/uk/computer-repair',
        'http://directory.thesun.co.uk/find/uk/computer-repair/page/2',
        'http://directory.thesun.co.uk/find/uk/computer-repair/page/3',
        'http://directory.thesun.co.uk/find/uk/computer-repair/page/4',
        'http://directory.thesun.co.uk/find/uk/computer-repair/page/5',
        'http://directory.thesun.co.uk/find/uk/computer-repair/page/6',
        'http://directory.thesun.co.uk/find/uk/computer-repair/page/7',
        'http://directory.thesun.co.uk/find/uk/computer-repair/page/8',
        'http://directory.thesun.co.uk/find/uk/computer-repair/page/9',
        'http://directory.thesun.co.uk/find/uk/computer-repair/page/10'
        ]
    

    
# the parse procedure, and here is the codes which declares which field to scrap. 
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@class="abTbl "]')
        items = []
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
            items.append(item)
        return items

 
