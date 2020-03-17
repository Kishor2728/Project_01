"""Project23_StudentApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Homeindex, name='Homeindex'),
    path('studentLogin/',views.studentLogin , name='studentLogin'),
    path('studentRegister/',views.studentRegister, name='studentRegister'),
    path('forgotPassword/',views.forgotPassword, name='forgotPassword'),
    path('showpass/',views.showpass,name='showpass'),

    path('studentLoginPage/',views.studentLoginCheck,name='studentLoginCheck'),
    path('studentHomePage/',views.studentHomePage, name='studentHomePage'),
    path('studentRegistered/',views.studentRegistered,name='studentRegistered'),
    path('viewProfile/',views.viewProfile,name='viewProfile'),
    path('updateProfile/',views.updateProfile,name='updateProfile'),
    path('profileUpdated/',views.profileUpdated, name='profileUpdated'),

    path('adminLogin/',views.adminLogin,name='adminLogin'),
    path('adminHome/',views.adminHome,name='adminHome'),
    path('viewAllStudents/',views.viewAllStudents,name='viewAllStudents'),
    path('deleteStudent/',views.deleteStudent,name='deleteStudent'),
    path('delete/',views.delete,name='delete'),
]
