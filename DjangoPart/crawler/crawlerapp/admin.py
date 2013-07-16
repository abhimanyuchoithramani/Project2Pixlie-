# This page is for the Admin settings.
from crawlerapp.models import *
from django.contrib import admin
#the below lines registers the models to admin.
admin.site.register(Directory)
admin.site.register(Adress)
admin.site.register(Photos)
