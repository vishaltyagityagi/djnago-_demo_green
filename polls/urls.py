from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import patterns, include, url
from polls.views import *

urlpatterns = [
url(r'^admin/', include(admin.site.urls)),
	# url(r'^polls/', include('polls.urls')),
	url(r'^$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', logout_page),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
	url(r'^register/$', register),
	url(r'^register/success/$', register_success),
	# url(r'^home/$', index),
	url(r'^search/$', search),
	url(r'^new_product/$', new_product),
	# url(r'^usermanagement/$', usermanagement),
	url(r'^delete/$', delete),
	url(r'^new_user/$', new_user),
	url(r'^userdelete/$', userdelete),
	url(r'^usersearch/$', usersearch),
	url(r'^(?P<post_id>[\d-]+)/edit/$', edit),
	url(r'^(?P<post_id>[\d-]+)/edituser/$', edit_user),
	url(r'^home/$', PostListView.as_view(), name='post_list'),
	url(r'^usermanagement/$', ProductListView.as_view(), name='product_list'),
	url(r'^(?P<post_id>[\d-]+)/show/$',show_product),
	url(r'^(?P<post_id>[\d-]+)/showuser/$',show_user),
	# url(r'^service/$', service),
	url(r'^new_service/$', new_service),
	url(r'^servicemanagement/$', ServiceListView.as_view(), name='service_list'),
	url(r'^(?P<post_id>[\d-]+)/editservice/$', edit_service),
	url(r'^(?P<post_id>[\d-]+)/showservice/$',show_service),
	url(r'^servicedelete/$', servicedelete),
	url(r'^servicesearch/$', servicesearch),

	#content management

	url(r'^new_content/$', new_content),
	url(r'^contentmanagement/$', ContentListView.as_view(), name='content_list'),
	url(r'^(?P<post_id>[\d-]+)/editcontent/$', edit_content),
	url(r'^(?P<post_id>[\d-]+)/showcontent/$',show_content),
	url(r'^contentdelete/$', contentdelete),
	url(r'^contentsearch/$', contentsearch),

	#email management

	url(r'^new_email/$', new_email),
	url(r'^emailmanagement/$', EmailListView.as_view(), name='email_list'),
	url(r'^(?P<post_id>[\d-]+)/editemail/$', edit_email),
	url(r'^(?P<post_id>[\d-]+)/showemail/$',show_email),
	url(r'^emaildelete/$', emaildelete),
	url(r'^emailsearch/$', emailsearch),

	#cms management

	url(r'^new_cms/$', new_cms),
	url(r'^cmsmanagement/$', CmsListView.as_view(), name='cms_list'),
	url(r'^(?P<post_id>[\d-]+)/editcms/$', edit_cms),
	url(r'^(?P<post_id>[\d-]+)/showcms/$',show_cms),
	url(r'^cmsdelete/$', cmsdelete),
	url(r'^cmssearch/$', cmssearch)


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
