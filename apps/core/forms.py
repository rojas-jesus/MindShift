from django import forms
from django.utils.translation import gettext_lazy as _
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
        exclude = ["duration_total"]
        help_texts = {
                "hour": _("If the thought lasted less than an hour, you can skip this field."),
                "minute": _("If the thought lasted less than a minute, you can skip this field."),
                "second": _("Indicate how long the thought lasted in seconds. If you have already specify the hour or minute fields, you can leave this field blank."),
                }
        widgets = {
            "timestamp": forms.widgets.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class":"form-control form-control-sm"
                    }
            ),
            "hour": forms.widgets.NumberInput(
                attrs={
                    "class": "form-control form-control-sm"}
            ),
            "minute": forms.widgets.NumberInput(
                attrs={
                    "class": "form-control form-control-sm"}
            ),
            "second": forms.widgets.NumberInput(
                attrs={
                    "class": "form-control form-control-sm"}
            ),
            "thought": forms.widgets.Select(
                attrs={
                    "class": "form-control form-control-sm"}
            )
        }




# Action Forms
class ActionForm(forms.ModelForm):
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

