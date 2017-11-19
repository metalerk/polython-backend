from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views
 
 
urlpatterns = [
    url(r'^users/list/$', views.ListUsers.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9a-f-]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^users/login/$', views.LoginUser.as_view(), name='user-login'),
    url(r'^users/create/$', views.CreateUser.as_view(), name='user-create'),
]