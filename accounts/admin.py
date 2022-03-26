from django.contrib import admin
from django.db import models
from accounts.models import User 

# Register your models here.
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
                "Personal info",
                {"fields": ("first_name", "last_name", "warehouse")},
        ),
        (
                "Permissions",
                {
                  "fields":(
                            "is_active",
                            "is_staff",
                            "is_manager",
                            "is_superuser",
                            "groups",
                            "user_permissions",
         )
                },
                ),
                (
                "Important dates",
                {"fields": ("last_login", "date_joined")},
                ),
                )
    add_fieldsets = (
                (
                None,
                {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
                },
                ),
                )
    list_display = (
                "email",
                "warehouse",
                "first_name",
                "last_name",
                "is_staff",
                "is_active"
                )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email"),
                                            
admin.site.register(User, UserAdmin) 
