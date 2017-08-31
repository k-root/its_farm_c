# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Farmer(models.Model):
	Name=models.CharField(max_length=50)
	Gender=models.CharField(max_length=15)
	Age=models.IntegerField()


class Member(models.Model):
	F_id=models.ForeignKey(Farmer, on_delete=models.CASCADE)
	Name=models.CharField(max_length=50)
	Gender=models.CharField(max_length=15)
	Age=models.IntegerField()
	Relation=models.CharField(max_length=15, default='')


class HouseHold(models.Model):
	F_id=models.ForeignKey(Farmer, on_delete=models.CASCADE,default='')
	Lat=models.CharField(max_length=15)
	Lon=models.CharField(max_length=15)
	Income=models.IntegerField()
