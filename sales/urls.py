from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from sales import views
 
 
urlpatterns = [
	url(r'^sales/create/$', views.CreateSale.as_view(), name='store-create'),
    url(r'^sales/update/(?P<pk>[0-9a-f-]+)/$', views.UpdateSale.as_view(), name='store-update'),
]