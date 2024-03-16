from rest_framework import serializers
from .models import Facilitator

class FacilitatorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Facilitator
        fields = ("id","name","description")
