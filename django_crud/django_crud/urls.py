# """django_crud URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import url,include
#
# from blog_posts import urls
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^blog_posts/',include(urls,namespace='blog_posts')),
#     # url(r'^$',home,name='home')
# ]


"""
Crudapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
     https://docs.djangoproject.com/en/1.11/topics/http/urls/
 """
from django.conf.urls import url, include
from django.contrib import admin
# from django_crud.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^blog_posts/', include('blog_posts.urls', 'blog_posts')),
    url(r'^blog_posts/', include(('blog_posts.urls','blog_posts'), namespace='blog_posts')),
    # url(r'^$', home, name='home' ),
]