from django.conf.urls import patterns, include, url
import dj_simple_sms
import API
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smsAPI.views.home', name='home'),
    # url(r'^smsAPI/', include('smsAPI.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sms/', include(dj_simple_sms.urls)),
    url(r'^api/',include('API.urls')),
)
