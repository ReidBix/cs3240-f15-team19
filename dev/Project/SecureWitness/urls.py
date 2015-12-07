# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from Project.SecureWitness import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^reports/([0-9]*)\/*$', views.reports, name='reports'),
    #url(r'^list/$', views.list, name='list'),                               #need to get rid of later
    url(r'^add_report/$', views.add_report, name='add_report'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^register/$', views.register, name='register'),
    url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^auth/$',views.auth, name='auth'),
    url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
    url(r'^search/', views.search, name='search'),
    url(r'^disp_report/([0-9]+)/$', views.disp_report, name="disp_report"),
    url(r'^edit_report/([0-9]+)/$', views.edit_report, name="edit_report"),
)

