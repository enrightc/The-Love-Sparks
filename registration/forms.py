from django import forms
from .models import LoveRegistration

class LoveRegistrationForm(forms.ModelForm):
    class Meta:
        model = LoveRegistration
        fields = ['name', 'email', 'gender', 'looking_for', 'age', 'location', 'bio']
