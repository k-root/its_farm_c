from rest_framework import serializers
from .models import *

class FarmerSerializer(serializers.ModelSerializer):
	class Meta:
		model=Farmer
		

class MemberSerializer(serializers.ModelSerializer):
	class Meta:
		model=Member 
		
class HouseHoldSerializer(serializers.ModelSerializer):
	class Meta:
		model=HouseHold
		