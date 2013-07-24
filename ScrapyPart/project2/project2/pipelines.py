
from scrapy import log

from twisted.enterprise import adbapi

import MySQLdb.cursors

# the required Pipeline settings.
class MySQLStorePipeline(object):

    def __init__(self):
        #   db settings
        
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                db='project2',
                user='root',
                passwd='',
                host='127.0.0.1',
                port='3306',                            
                cursorclass=MySQLdb.cursors.DictCursor,
                charset='utf8',
                use_unicode=True
            )

def process_item(self, item, spider):
    # run db query in thread pool
    query = self.dbpool.runInteraction(self._conditional_insert, item)
    query.addErrback(self.handle_error)
    return item

    
def _conditional_insert(self, tx, item):
    #runs the condition
    insert_id = tx.execute(\
        "insert into crawlerapp_directory (Catogory, Bussiness_name, Description, Number, Web_url) "
        "values (%s, %s, %s, %s, %s)",
        (item['Catogory'][0],
         item['Bussiness_name'][0],
         item['Description'][0],
         item['Number'][0],
         item['Web_url'][0],
         )
        )
    #connection to the foreign key Adress.
    tx.execute(\
        "insert into crawlerapp_adress (directory_id, adress_name) "
        "values (%s, %s)",
        (insert_id,
         item['adress_name'][0]
         )
        )
    #connection to the foreign key Photos.
    tx.execute(\
        "insert into crawlerapp_photos (directory_id, Photo_path, Photo_name) "
        "values (%s, %s, %s)",
        (insert_id,
         item['Photo_path'][0],
         item['Photo_name'][0]
         )
        )
    log.msg("Item stored in db: %s" % item, level=log.DEBUG)
def handle_error(self, e):
    log.err(e)
