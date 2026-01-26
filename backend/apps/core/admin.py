from django.contrib import admin
from .models import Thought, ThoughtDate, Facilitator, Action, ActionDate, Environment, VoiceThoughtEntry

admin.site.register(Thought)
admin.site.register(ThoughtDate)

admin.site.register(Facilitator)
admin.site.register(Action)
admin.site.register(Environment)
admin.site.register(VoiceThoughtEntry)

@admin.register(ActionDate)
class ActionDateAdmin(admin.ModelAdmin):
    exclude = ["duration_total"]

