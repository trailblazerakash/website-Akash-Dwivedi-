from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'website.views.home', name='home'),
     url(r'^home/', 'website.views.home', name='home'),
     url(r'^about/', 'website.views.about', name='about'),
     url(r'^career/', 'career.views.career', name='career'),
     url(r'^gallery/', 'website.views.gallery', name='gallery'),
     url(r'^contact/', 'contact.views.contact', name='contact'),
     url(r'^Page_Not_Found/', 'website.views.Page_Not_Found', name='Page_Not_Found'),
     url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)