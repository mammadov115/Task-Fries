from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Project)
admin.site.register(Workspace)
admin.site.register(Task)
admin.site.register(TaskCategory)
