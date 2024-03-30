from rest_framework import serializers
from .models import Facilitator, Environment

class FacilitatorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Facilitator
        fields = ("id","name","description","user")

class EnvironmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Environment
        fields = ("id","name","description")

