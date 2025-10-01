from rest_framework import serializers
from .models import Facilitator, Environment, Thought

class ThoughtSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Thought
        fields = ("id","name","description","advantages","disadvantages",
                  "facilitator","thought_facilitator","action_facilitator",
                  "environment_facilitator")

class FacilitatorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Facilitator
        fields = ("id","name","description","user")

class EnvironmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Environment
        fields = ("id","name","description")

