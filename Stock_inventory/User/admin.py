from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import (
    Department,
    Position,
    UserInfo
)
# Register your models here.

User = get_user_model()


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = [
        'department_name'
    ]

    list_display = [
        'department_name',
        'slug',
        'created'
    ]
    fields = [
        'department_name',
        'slug',
        'created'
    ]
    readonly_fields = [
        'slug',
        'created'
    ]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    search_fields = [
        'position_name'
    ]

    list_display = [
        'position_name',
        'slug',
        'created'
    ]
    fields = [
        'position_name',
        'slug',
        'created'
    ]
    readonly_fields = [
        'slug',
        'created'
    ]


class UserInfoTabularInline(admin.TabularInline):
    model = UserInfo
    max_num = 1


@ admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = [
        UserInfoTabularInline
    ]
