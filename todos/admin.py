from django.contrib import admin
from . import models


@admin.register(models.Todo)
class TodoAdmin(admin.ModelAdmin):

    list_display = ("title",)
