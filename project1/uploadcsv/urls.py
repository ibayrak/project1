# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('project1.uploadcsv.views',
    url(r'^home/$', 'home', name='home'),
)
