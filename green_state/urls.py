from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import patterns, include, url
from green_state.views import *



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    url(r'^about_us/$', about_us),
    # url(r'^services/$', services),
    url(r'^solutions/$', solutions),
    url(r'^support/$', support),
    # Contact us page work
    url(r'^contact_us/$', contact_us),
    url(r'^username_exist/$', username_exist),
    url(r'^contactsuccess/$', contactsuccess),
    url(r'^supportsuccess/$', supportsuccess),
    # url(r'^/green/', 'django.contrib.auth.views.login'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
