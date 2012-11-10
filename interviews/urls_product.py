from django.conf.urls.defaults import patterns, url
from interviews.views import ProductDetailView, ProductListView
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = patterns('interviews.views',
    url(r'^$', staff_member_required(ProductListView.as_view()), name='product-list'),
    url(r'^(?P<slug>[-\w]+)$', staff_member_required(ProductDetailView.as_view()), name='product-detail'),
)
