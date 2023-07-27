"""djangoPractice URL Configuration

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
from blog import views
from blog.views import LoginUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(),name='home'),
    path('articles/<slug:article_slug>', views.ArticalPage.as_view(), name='article_page'),#считать осюда, ниже нужно просто для шаблона
    path('about/', views.about_page, name='about'),
    path('addpage/', views.add_page, name='add_page'),
    path('contact/', views.home_page, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', views.home_page, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', views.home_page, name='post'),
    path('category/<slug:cat_slug>/', views.home_page, name='category'),
]
