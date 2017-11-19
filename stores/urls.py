from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from stores import views
 
 
urlpatterns = [
    url(r'^stores/$', views.StoreList.as_view(), name='store-list'),
    url(r'^stores/(?P<pk>[0-9a-f-]+)/$', views.StoreDetail.as_view(), name='store-detail'),
]