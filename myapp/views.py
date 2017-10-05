# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
import urllib, json
import requests


# Create your views here.
def index(request):
	return HttpResponse('<h2>The Index of Myapp..</h2>')


def maps(request):
	markers1=[{'lat':-33.7772, 'long':151.1241}]
	return render(request, 'myapp/abc.html',{'point':markers1})



class HouseHoldList(APIView):
	def get(self, request):
		hhlist = HouseHold.objects.all()
		serializer=HouseHoldSerializer(hhlist, many=True)
		return Response(serializer.data)
	def post(self):
		pass

def retrieve_farmer(request):
	url = "http://kr00t.pythonanywhere.com/farmer/?format=json"
	response=urllib.urlopen(url)
	data = response.read()
	return HttpResponse(data)

def retrieve_household(request):
	url = "http://kr00t.pythonanywhere.com/household/?format=json"
	response=urllib.urlopen(url)
	data = response.read()
	return HttpResponse(data)

def retrieve_member(request):
	url = "http://kr00t.pythonanywhere.com/member/?format=json"
	response=urllib.urlopen(url)
	data = response.read()
	return HttpResponse(data)

def retrievefarmer_detail(request,pk):
	i=pk
	url = "http://kr00t.pythonanywhere.com/farmerid/"+str(i)+"/?format=json"
	response=urllib.urlopen(url)
	data = response.read()
	return HttpResponse(data)

def retrievehousehold_detail(request,pk):
	i=pk
	url = "http://kr00t.pythonanywhere.com/householdid/"+str(i)+"/?format=json"
	response=urllib.urlopen(url)
	data = response.read()
	return HttpResponse(data)

def retrievemember_detail(request,pk):
	i=pk
	url = "http://kr00t.pythonanywhere.com/memberid/"+str(i)+"/?format=json"
	response=urllib.urlopen(url)
	data = response.read()
	return HttpResponse(data)

def retrieveabc(request):
	url = "http://10.0.3.23:8989/maplist/?format=json"
	response=urllib.urlopen(url)
	jsondata=json.loads(response.read())

	url_farmer="http://10.0.3.23:8989/farmer/?format=json"
	response_farmer=urllib.urlopen(url_farmer)
	jsondata_farmer=json.loads(response_farmer.read())

	url_farm="http://10.0.3.23:8989/farms/?format=json"
	response_farm=urllib.urlopen(url_farm)
	jsondata_farm=json.loads(response_farm.read())

	url_household="http://10.0.3.23:8989/household/?format=json"
	response_household=urllib.urlopen(url_household)
	jsondata_household=json.loads(response_household.read())

	url_wells="http://10.0.3.23:8989/wells/?format=json"
	response_wells=urllib.urlopen(url_wells)
	jsondata_wells=json.loads(response_wells.read())

	return render(request, 'myapp/abc.html',{'points':jsondata,'wells':jsondata_wells , 'farmers':jsondata_farmer, 'farms':jsondata_farm, 'houses':jsondata_household})
