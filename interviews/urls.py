from django.conf.urls.defaults import patterns, url
from interviews.views import InterviewListView, InterviewDetailView

urlpatterns = patterns('interviews.views',
    url(r'^$', InterviewListView.as_view(), name='interviews-list'),
    url(r'^page-(?P<page>\d+)/$', InterviewListView.as_view(), name='interviews-list-page'),
    url(r'^(?P<slug>[-\w]+)/$', InterviewDetailView.as_view(), name='interviews-detail'),
)
