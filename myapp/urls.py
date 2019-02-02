"""myapp URL Configuration

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
from django.views.generic import TemplateView
from scouts.views import scout_form, scout_thanks, scout_all


urlpatterns = [
    path('home/', TemplateView.as_view(template_name='myapp/scout_form.html'), name='home'),
    path('admin/', admin.site.urls),
    path('scout/', scout_form, name='scout'),
    path('thanks/', scout_thanks, name='thanks'),
    path('', scout_all, name='all')
]
