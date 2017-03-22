"""set2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from wikiapp import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^start/', views.question1),
    url(r'^050317/', views.question2),
    url(r'^Kiribati/', views.question3),
    url(r'^cook/', views.question4),
    url(r'^I_Love_Bees/', views.question5),
    url(r'^36KL49/', views.question6),
    url(r'^Brazil/', views.question7),
    url(r'^Aditi/', views.question8),
    url(r'^Sita/',views.question9),
    url(r'^Agrippa/', views.question10),
    url(r'^The_Dalek_Emperor/', views.question11),
    url(r'^Mithila/', views.question12),
    url(r'^Cicada/', views.question13),
    url(r'^4/', views.question14),
    url(r'^name/', views.end),
]
