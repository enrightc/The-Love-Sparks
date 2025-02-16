from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = (
        "username", "email", "gender", "looking_for", "age",
        "free_time_preference", "friends_description", "relationship_excites",
        "is_active", "is_staff"
    )

admin.site.register(CustomUser, CustomUserAdmin)