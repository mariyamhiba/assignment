"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_home', views.admin_home, name='admin_home'),

    path('admin_change', views.admin_change, name='admin_change'),

    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('user_login', views.user_validation, name='user_login'),
    path('user_reg', views.user_reg, name='user_reg'),
    path('user_home', views.user_home, name='user_home'),
    path('user_change', views.user_change, name='user_change'),
    path('user_logout', views.user_logout, name='user_logout'),


    path('admin_users_view', views.admin_users_view, name='admin_users_view'),
    path('admin_add', views.admin_add, name='admin_add'),
    path('admin_studdetails_view', views.admin_studdetails_view, name='admin_studdetails_view'),
    path('admin_delete_stud', views.admin_delete_stud, name='admin_delete_stud'),


]
