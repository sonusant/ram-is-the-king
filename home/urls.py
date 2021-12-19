from django.contrib import admin
from django.urls import path 
from home import views
from django.conf.urls import url



urlpatterns = [
    path('', views.index, name='home'),
    path('ram', views.ram, name='ram'),
    path('laxman', views.laxman, name='laxman'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('signup', views.signup, name='signup'),
]
