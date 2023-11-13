from django import forms
from .models import Thought, ThoughtDate


class CreateThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = "__all__"
        widgets = {
            "name": forms.widgets.TextInput(
                attrs={
                    "placeholder": "Provide name thought",
                    "autocomplete": "off",
                    "class": "form-control form-control-sm",
                }
            ),
            "thought_intensity": forms.widgets.Select(
                attrs={"class": "form-control form-control-sm"}
            ),
            "description": forms.widgets.Textarea(
                attrs={
                    "placeholder": "Provide thought description ",
                    "rows": 3,
                    "class": "form-control form-control-sm",
                }
            ),
            "advantages": forms.widgets.Textarea(
                attrs={
                    "placeholder": "Provide thought advantages",
                    "rows": 3,
                    "class": "form-control form-control-sm",
                }
            ),
            "disadvantages": forms.widgets.Textarea(
                attrs={
                    "placeholder": "Provide thought disadvantages",
                    "rows": 3,
                    "class": "form-control form-control-sm",
                }
            ),
            "emotion": forms.widgets.Select(
                attrs={"class": "form-control form-control-sm"}
            ),
            "emotion_intensity": forms.widgets.Select(
                attrs={"class": "form-control form-control-sm"}
            ),
        }


class CreateThoughtDateForm(forms.ModelForm):
    class Meta:
        model = ThoughtDate
        fields = "__all__"
        widgets = {
            "timestamp": forms.widgets.DateTimeInput(attrs={"type": "datetime-local"})
        }
