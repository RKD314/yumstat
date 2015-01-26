from django.conf.urls import patterns, url

from site_flow import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
)
