from django import forms
from .models import Thought, ThoughtDate


class CreateThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = "__all__"
        widgets = {
            "name": forms.widgets.TextInput(
                attrs={"placeholder": "Provide name thought"}
            ),
            "description": forms.widgets.Textarea(
                attrs={"placeholder": "Provide thought description "}
            ),
            "advantages": forms.widgets.Textarea(
                attrs={"placeholder": "Provide thought advantages"}
            ),
            "disadvantages": forms.widgets.Textarea(
                attrs={"placeholder": "Provide thought disadvantages"}
            ),
        }


class CreateThoughtDateForm(forms.ModelForm):
    class Meta:
        model = ThoughtDate
        fields = "__all__"
        widgets = {
            "timestamp": forms.widgets.DateTimeInput(attrs={"type": "datetime-local"})
        }
