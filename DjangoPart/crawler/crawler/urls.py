from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crawler.views.home', name='home'),
    # url(r'^crawler/', include('crawler.foo.urls')),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #the below line helps the user to navigate pages.
    url(r'^crawlerapp/$', 'crawlerapp.views.index'),
    url(r'^crawlerapp/contactus/$', 'crawlerapp.views.contactus'),
    url(r'^crawlerapp/search/$', 'crawlerapp.views.search'),
)
