__author__ = 'ras-al-ghul'
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'career.views.career', name='career'),

     url(r'^(?P<project_name_slug>[\w\-]+)/$', 'career.views.project', name='project'),
)
