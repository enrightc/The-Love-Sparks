from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from datetime import date

class CustomUserCreationForm(UserCreationForm):
    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 18:
            raise forms.ValidationError("You must be at least 18 years old to sign up.")
        return age

    class Meta:
        model = CustomUser
        fields = (
            "username", "email", "gender", "looking_for", "age",
            "free_time_preference", "friends_description", "relationship_excites",
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username", "email", "gender", "looking_for", "age",
            "free_time_preference", "friends_description", "relationship_excites",
        )
