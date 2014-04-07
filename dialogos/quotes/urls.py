from django.conf.urls import patterns, url

from quotes import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)