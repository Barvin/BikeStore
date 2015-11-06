from django.conf.urls import patterns, url

urlpatterns = patterns('',
                      url(r'^$', 'products.views.all_products'),
                      url(r'(?P<product_id>\d+)/$', 'products.views.product'),
                      )
