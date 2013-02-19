from django.conf.urls.defaults import patterns, url
from ..views import InterviewListView, InterviewDetailView, PreviewInterviewDetailView

urlpatterns = patterns('interviews.views',
    url(r'^$', InterviewListView.as_view(), name='interviews-list'),
    url(r'^preview/(?P<hash>[\w]+)/(?P<slug>[-\w]+)$', PreviewInterviewDetailView.as_view(), name='interviews-preview'),
    url(r'^page-(?P<page>\d+)/$', InterviewListView.as_view(), name='interviews-list-page'),
    url(r'^(?P<filter_key>\w+)-(?P<filter_value>\w+)/$', InterviewListView.as_view(), name='interviews-list-filter'),
    url(r'^(?P<slug>[-\w]+)$', InterviewDetailView.as_view(), name='interviews-detail'),
)
