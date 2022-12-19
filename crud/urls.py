"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app1 import views as app1_views
from . import views as project_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1_views.home,name='home'),
    path('delete/<int:id>', app1_views.delete,name='delete'),
    path('edit/<int:id>', app1_views.edit,name='edit'),
    path('signup/', project_views.sign_up,name='sign_up'),
]