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
	url = "http://kr00t.pythonanywhere.com/member/"+str(i)+"/?format=json"
	response=urllib.urlopen(url)
	data = response.read()
	return HttpResponse(data)

