from django.conf.urls.defaults import patterns, url
from interviews.views import ProductDetailView

urlpatterns = patterns('interviews.views',
    
    url(r'^(?P<slug>[-\w]+)$', ProductDetailView.as_view(), name='product-detail'),
)
