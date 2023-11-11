from django import forms
from .models import Thought, ThoughtDate


class CreateThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = "__all__"
        widgets = {
            "name": forms.widgets.TextInput(
                attrs={"placeholder": "Provide name thought",
                       "autocomplete":"off",
                       "class":"form-control"}
            ),
            "thought_intensity": forms.widgets.Select(
                attrs={"class":"form-control"}
            ),
            "description": forms.widgets.Textarea(
                attrs={"placeholder": "Provide thought description ",
                       "class":"form-control"}
            ),
            "advantages": forms.widgets.Textarea(
                attrs={"placeholder": "Provide thought advantages",
                       "class":"form-control"}
            ),
            "disadvantages": forms.widgets.Textarea(
                attrs={"placeholder": "Provide thought disadvantages",
                       "class":"form-control"}
            ),
            "emotion": forms.widgets.Select(
                attrs={"class":"form-control"}
            ),
            "emotion_intensity": forms.widgets.Select(
                attrs={"class":"form-control"}
            )
        }


class CreateThoughtDateForm(forms.ModelForm):
    class Meta:
        model = ThoughtDate
        fields = "__all__"
        widgets = {
            "timestamp": forms.widgets.DateTimeInput(attrs={"type": "datetime-local"})
        }
