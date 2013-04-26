from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

urlpatterns = patterns('API.views',
    url(r'^sendsms/(?P<from_number>.*?)/(?P<to>.*?)/(?P<body>.*?)/$','sendSMS'),

)