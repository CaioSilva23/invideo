from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Users
from .forms import UserChangeForm, UserCreationForm


class UserModelAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    list_display = ["id", "email", "get_full_name", "is_staff"]
    list_filter = ["is_staff"]
    fieldsets = BaseUserAdmin.fieldsets + (

    )
    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = []

admin.site.register(Users, UserModelAdmin)
