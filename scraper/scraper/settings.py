import sys
import os

sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'newsbot.settings'

import django
django.setup()


BOT_NAME = 'scraper'

SPIDER_MODULES = ['scraper.spiders']

ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {"scraper.pipelines.ScraperPipeline": 300}