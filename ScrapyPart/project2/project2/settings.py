# Scrapy settings for project2 project

# For simplicity, this file contains only the most important settings by
# default. 


BOT_NAME = 'project2'

SPIDER_MODULES = ['project2.spiders']
NEWSPIDER_MODULE = 'project2.spiders'

ITEM_PIPELINES = (
    'project2.pipelines.MySQLStorePipeline',
)

