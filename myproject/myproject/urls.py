"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from posts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('movies/', show_movies, name='show_movies'),
    path('movies/login', login, name='login'),
    path('movies/register/', register, name='register'),
    path('movies/logout/', logout_page, name='logout_page'),
    path('movies/add_movie/', add_movie, name='add_movie'),
    path('movies/add_cast/', add_cast, name='add_cast'),
    path('movies/delete_movie/<int:id>/', delete_movie, name='delete_movie'),
    path('movies/showdetails/<int:id>',show_details,name='show_details'),
    path('movies/search/',search_movie,name='search_movie')
]
