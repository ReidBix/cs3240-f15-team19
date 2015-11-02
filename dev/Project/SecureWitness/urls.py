# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from Project.SecureWitness import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^list/$', views.list, name='list'),
    url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
    #url(r'^adduser/$', views.adduser, name='adduser' ),
)