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


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [AssignedPersonInline]


@admin.register(AssignedPersonProxy)
class AssignedPersons(admin.ModelAdmin):
    readonly_fields = ['start_date', 'end_date', 'task', 'user']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)

    def has_module_permission(self, request):
        return request.user.username != 'admin'

