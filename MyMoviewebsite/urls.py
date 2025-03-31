"""
URL configuration for MyPro project.

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
from MyMoviewebsite import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, ),
    path('sign/', views.sign),
    path('login/', views.login),
    path('head/', views.header),
    path('footer/', views.footer),
    path('adminmain/',views.adminmain),
    path('movielist/',views.movielist),
    path('addmovies/',views.addmovies),
    path('trending/',views.trending),
    path('crausal/',views.crausal),
    path('englishh/',views.english),  
    path('hindih/',views.hindi),
    path('marathih/',views.marathi),
    path('southh/',views.south),
    path('allmovies/',views.allmovies),
    path('movie/<int:unique>',views.movie , name='movie'),
    path('loginlist/',views.loginlist),
    path('myupdate/',views.MyUpdate),
    path('update/',views.Update,name='update'),
    path('del/',views.MyDelete),
]
