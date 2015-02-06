from django.contrib import admin
from challenge.models import Goal, GoalInstance, SignificantOther

# Register your models here.
admin.site.register(Goal)
admin.site.register(GoalInstance)
admin.site.register(SignificantOther)
