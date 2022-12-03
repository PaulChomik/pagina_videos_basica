"""projecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.feed,name='feed'),
    path('profile/',views.profile,name='profile'),
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout'), #para poder redireccionar el formulario hay que poner en settings.py LOGIN_REDIRECT
    path('movie_details/<str:movie_name>/',views.movie_details,name='movie_details'),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
tenia un error en el cual definia por defecto la ruta de los archivos staticos 
como static_url ,pero en settings ponia media_url
'''

#static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # this is to manage static files
