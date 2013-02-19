from django.conf.urls.defaults import patterns, url
from interviews.views import ProductDetailView, ProductListView

urlpatterns = patterns('interviews.views',
    url(r'^$', ProductListView.as_view(), name='product-list'),
    url(r'^page-(?P<page>\d+)/$', ProductListView.as_view(), name='product-list-page'),
    url(r'^(?P<slug>[-\w]+)$', ProductDetailView.as_view(), name='product-detail'),
)
