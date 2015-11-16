# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from Project.SecureWitness import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^list/$', views.list, name='list'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^register/$', views.register, name='register'),
    url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^auth/$',views.auth, name='auth'),
    (r'^messages/', include('postman.urls', namespace='postman', app_name='postman'))
)
