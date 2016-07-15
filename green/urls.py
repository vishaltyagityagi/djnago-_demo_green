from django.conf.urls import patterns, include, url
from django.contrib import admin
# from green_state.views import *
# from .views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'green.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^green/', include('green_state.urls')),
    url(r'^service/', include('services.urls')),
	url(r'^homelogin/', 'django.contrib.auth.views.login'),

    # url(r'^home/', 'django.contrib.auth.views.login'),
	# url(r'^home/', 'django.contrib.auth.views.login'),


    url(r'^', include('polls.urls')),

)
