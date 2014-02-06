from django.conf.urls import patterns, include, url
from rango import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
    url(r'^about/',views.about, name='about'),
)
