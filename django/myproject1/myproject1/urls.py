"""myproject1 URL Configuration

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
from django.contrib import admin
from django.urls import path
from covid import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('sir/',views.tom,name='tom'),
    path('reg/',views.reg, name='reg'),
    path('student_reg/',views.student_reg,name="student_reg"),
    path('',views.home,name='home'),
    path('display/',views.display,name='display'),
    path('edit/<str:id>',views.edit,name='edit'),
    path('update/<str:id>',views.update,name="update"),
    path('del/<str:id>',views.deld,name="del"),
    
]
