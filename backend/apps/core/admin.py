from django.contrib import admin
from .models import Thought, ThoughtDate, Facilitator, Action, ActionDate, Environment, ThoughtRaw, ActionRaw

admin.site.register(Thought)
admin.site.register(ThoughtDate)

admin.site.register(Facilitator)
admin.site.register(Action)
admin.site.register(Environment)
admin.site.register(ThoughtRaw)
admin.site.register(ActionRaw)

@admin.register(ActionDate)
class ActionDateAdmin(admin.ModelAdmin):
    exclude = ["duration_total"]

