from django.conf.urls import url
from django.contrib import admin
from dogs import views
from django.contrib.auth import views as auth_views
from django.conf.urls import include

app_name = 'dogs'

urlpatterns = [
    url(r'^/', include('django.contrib.auth.urls')),
    url(r'^accounts/signup/$', views.signup, name='signup'),
    url(r'^login/$', views.signin, name='login'),
]
