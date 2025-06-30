from django.contrib import admin
from .models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'priority', 'status', 'due_date')
    list_filter = ('priority', 'status', 'due_date')
    search_fields = ('title', 'description')
