from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^site/', include('site_flow.urls', namespace="site_flow")),
    url(r'^simple/', include('simple.urls', namespace="simple")),
    url(r'^admin/', include(admin.site.urls)),
)
