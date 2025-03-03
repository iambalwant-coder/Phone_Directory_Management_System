"""
URL configuration for Phone_Directory_Management_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Contact_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add_contact/', views.add_contact, name='add_contact'),
     path('view_all/', views.view_all, name='view_all'), 
    path('delete/<int:id>/', views.delete_contact, name='delete_contact'),  
    path('edit/<int:id>/', views.edit, name='edit'),
    path('trash/', views.trash, name='trash'),
]
