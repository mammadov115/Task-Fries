from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Project)
admin.site.register(Workspace)
admin.site.register(TaskCategory)


class AssignedPersonInline(admin.StackedInline):
    model = AssignedPerson
    extra = 1
    readonly_fields = ['user_start_date', 'user_end_date']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ['user', 'start_date', 'end_date', 'description']
        else:
            return []


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [AssignedPersonInline]

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ['project', 'category', 'task_start_date', 'task_end_date', 'task_priority', 'description']
        else:
            return []

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(assignedperson__user=request.user)
        return qs

# @admin.register(AssignedPersonProxy)
# class AssignedPersons(admin.ModelAdmin):
#     readonly_fields = ['start_date', 'end_date', 'task', 'user', 'description']
#
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         return qs.filter(user=request.user)
#
#     def has_module_permission(self, request):
#         return request.user.username != 'admin'
