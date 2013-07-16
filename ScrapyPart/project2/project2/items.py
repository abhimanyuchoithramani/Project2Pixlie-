from scrapy.item import Item, Field
# here in the item class I have declaired the fields which that the scrapy will
# crawl and save in the respective attributes .
class Project2Item(Item):
    Catogory = Field()
    Bussiness_name = Field()
    Description = Field()
    Number = Field()
    Web_url = Field()
    adress_name = Field()
    Photo_name = Field()
    Photo_path = Field()
    
