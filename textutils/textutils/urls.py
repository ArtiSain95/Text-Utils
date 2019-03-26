"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

# urlpatterns = [
#         path('admin/', admin.site.urls),
#         path('', views.index, name='index'),
#         path('playlist1', views.playlist1, name='playlist1'),
#         path('playlist2', views.playlist2, name='playlist2'),
#         path('playlist3', views.playlist3, name='playlist3'),
#         path('playlist4', views.playlist4, name='playlist4'),
#         path('playlist5', views.playlist5, name='playlist5'),
#         path('about/', views.about, name='about')
#   ]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('removepunc', views.removepunc, name='rempun'),
#     path('capitalizefirst', views.capfirst, name='capfirst'),
#     path('newlineremove', views.newlineremove, name='newlineremove'),
#     path('spaceremove', views.spaceremove, name='spaceremove'),
#     path('charcount', views.charcount, name='charcount'),
#
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze')


]
