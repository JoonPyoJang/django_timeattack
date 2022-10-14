from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/',views.sign_up, name='signup-view'),
    path('login/',views.login_view, name='login-view'),
    path('',views.homepage, name='home'),
]
