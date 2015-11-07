from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from products import views

urlpatterns = patterns('',
                      url(r'^$', 'products.views.all_products'),
                      url(r'^(?P<product_id>\d+)/$', 'products.views.product'),
                      url(r'^api/(?P<pk>[0-9]+)/$', views.productInfo.as_view()),
                      )

urlpatterns = format_suffix_patterns(urlpatterns)
