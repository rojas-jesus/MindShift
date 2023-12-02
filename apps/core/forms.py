from django import forms
from .models import Thought, ThoughtDate, Action


class ThoughtForm(forms.ModelForm):
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


class ThoughtDateForm(forms.ModelForm):
    class Meta:
        model = ThoughtDate
        fields = "__all__"
        widgets = {
            "timestamp": forms.widgets.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class":"form-control form-control-sm"
                    }
            ),
            "duration": forms.widgets.NumberInput(
                attrs={
                    "class": "form-control form-control-sm"}
            ),
            "thought": forms.widgets.Select(
                attrs={
                    "class": "form-control form-control-sm"}
            )
        }




# Action Forms
class ActionCreateForm(forms.ModelForm):
    class Meta:
        model = Action
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
            "facilitator": forms.widgets.SelectMultiple(
                attrs={
                    "class": "form-control form-control-sm",
                    "id":"facilitator-choicesjs",
                }
            ),
            "thought_facilitator": forms.widgets.SelectMultiple(
                attrs={
                    "class": "form-control form-control-sm",
                    "id":"thought-facilitator-choicesjs"
                }
            ),
            "emotion": forms.widgets.Select(
                attrs={"class": "form-control form-control-sm",
                       "id":"emotion-choicesjs",
                       }
            ),
            "emotion_intensity": forms.widgets.Select(
                attrs={"class": "form-control form-control-sm"}
            ),
        }


class ActionUpdateForm(ActionCreateForm):
    pass
