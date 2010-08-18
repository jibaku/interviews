from django.conf.urls.defaults import *

urlpatterns = patterns('interviews.views',
    url(r'^(?P<interview_slug>[-\w]+)/$', 'interview_detail', name='interviews-detail'),
    url(r'^$', 'interview_list', name='interviews-list'),
)
