from django.contrib import admin

from apps.objective.models.objective import Objective

@admin.register(Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value')
