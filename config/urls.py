"""URL Configuration

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
from django.urls import include
from config.views import my_login_view, offline
from users.views import mainpage  # import your view at the top

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qr_code/', include('users.urls')),
    path('lecture/',include('lecture.urls')),
    path('login/', my_login_view, name='login'),
    path('posts/', include('posts.urls')),
    path('offline/', offline, name='offline'),
    path('sogang_gpt/', include('sogang_gpt.urls')),
    path(r'', mainpage, name='home'),
    path('', include('pwa.urls')),
]
