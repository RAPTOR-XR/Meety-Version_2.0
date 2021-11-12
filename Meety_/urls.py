"""Meety_ URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings 

from Profile.views import UserProfile, UserProfileFavorites, follow

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('Post.urls')),
    path('user/', include('Profile.urls')),
    path('direct/', include('Direct.urls')),
    path('stories/', include('Story.urls')),
    path('notifications/', include('Notification.urls')),
    path('<username>/', UserProfile, name='profile'),
    path('<username>/saved', UserProfile, name='profilefavorites'),
    path('<username>/follow/<option>', follow, name='follow'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
