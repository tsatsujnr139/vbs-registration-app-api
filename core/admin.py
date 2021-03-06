from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from core import models

from admin_export_action.admin import export_selected_objects


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "first_name", "last_name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser")},
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            "None",
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


@admin.register(models.Participant)
class ParticipantAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created",
        "modified",
    )
    list_display = (
        "first_name",
        "last_name",
        "age",
        "gender",
        "grade",
        "church",
        "parent_name",
        "session",
        "attendance_type",
    )
    list_filter = (
        "grade",
        "gender",
        "age",
        "session",
        "attendance_type",
    )
    search_fields = ("first_name", "last_name", "parent_name", "church")

    actions = [
        export_selected_objects,
    ]


@admin.register(models.Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created",
        "modified",
    )
    list_display = (
        "first_name",
        "last_name",
        "preferred_role",
        "email",
        "previous_volunteer",
        "church",
    )
    list_filter = (
        "preferred_role",
        "preferred_class",
        "previous_volunteer",
        "previous_site",
    )
    search_fields = ("first_name", "last_name")

    actions = [
        export_selected_objects,
    ]


@admin.register(models.Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.AttendanceType)
class AttendanceTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "start_date", "end_date")
