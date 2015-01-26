from django.conf.urls import patterns, url

from simple import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^original_index/', views.original_index, name='original_index'),
    url(r'^login/', views.login, {'provider_name': 'fb'}, name='login')
)
