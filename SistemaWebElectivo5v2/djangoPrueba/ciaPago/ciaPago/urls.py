"""ciaPago URL Configuration

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
from django.urls import path
from ciaPago.views import index
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf.urls import include
from django.http import HttpResponse
from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
@login_required

def home(request):
	return HttpResponse('hola mundo')

urlpatterns = [
	#url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
	#url(r'^$', RedirectView.as_view(url='index/login', permanent=False), name='login'),
    path('admin/', admin.site.urls),
    path('index/', include('django.contrib.auth.urls')),
    #path('inicio/', index),
    path('login/', index),
    path('accounts/profile/', home),
]
