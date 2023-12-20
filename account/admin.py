from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_superuser')

admin.site.register(Colleague)
admin.site.register(Customer)
admin.site.register(Freelancer)
admin.site.register(Admin)

