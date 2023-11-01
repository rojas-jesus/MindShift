from django import forms 
from .models import Thought, ThoughtDate 

class CreateThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = "__all__"

class CreateThoughtDateForm(forms.ModelForm):
    class Meta:
        model = ThoughtDate
        fields = "__all__"
        widgets = {
            "timestamp":forms.widgets.DateTimeInput(attrs={"type":"datetime-local"})         
        }

