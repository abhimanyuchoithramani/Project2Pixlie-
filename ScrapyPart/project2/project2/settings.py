# Scrapy settings for project2 project

# For simplicity, this file contains only the most important settings by
# default. 


BOT_NAME = 'project2'

SPIDER_MODULES = ['project2.spiders']
NEWSPIDER_MODULE = 'project2.spiders'

#this sets the crawling depth, here I am setting as 20 pages.
DEPTH_LIMIT = 20

ITEM_PIPELINES = (
    'project2.pipelines.MySQLStorePipeline',
)

