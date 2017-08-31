"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myapp/', include('myapp.urls')),
    url(r'^household/', views.HouseHoldList.as_view()),
    url(r'^retrievefarmerid/(?P<pk>[0-9]+)/$', views.retrievefarmer_detail),
    url(r'^retrievehouseholdid/(?P<pk>[0-9]+)/$', views.retrievehousehold_detail),
    url(r'^retrievememberid/(?P<pk>[0-9]+)/$', views.retrievemember_detail),
    url(r'^retrievefarmer/', views.retrieve_farmer, name='retrieve_farmer'),
    url(r'^retrievehousehold/', views.retrieve_household, name='retrieve_household'),
    url(r'^retrievemember/', views.retrieve_member, name='retrieve_member'),


]
urlpatterns=format_suffix_patterns(urlpatterns)