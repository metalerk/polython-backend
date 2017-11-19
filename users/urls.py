from django.conf.urls import url
from users import views
 
 
urlpatterns = [
    url(r'^users/list/$', views.ListUsers.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9a-f-]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^users/login/$', views.LoginUser.as_view(), name='user-login'),
    url(r'^users/logout/$', views.LogoutUser.as_view(), name='user-logout'),
    url(r'^users/create/$', views.CreateUser.as_view(), name='user-create'),
]