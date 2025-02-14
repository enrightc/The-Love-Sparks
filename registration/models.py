from django.db import models
from django.core.exceptions import ValidationError

class LoveRegistration(models.Model):
    GENDER_CHOICES = [
        ('man', 'Man'),
        ('woman', 'Woman'),
        ('non_binary', 'Non-Binary'),
        ('prefer_not_to_say', 'Prefer not to say'),
    ]

    LOOKING_FOR_CHOICES = [
        ('man', 'Man'),
        ('woman', 'Woman'),
        ('non_binary', 'Non-Binary'),
        ('any', 'Any'),
    ]

    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True, blank=False)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, blank=False)
    looking_for = models.CharField(max_length=50, choices=LOOKING_FOR_CHOICES, blank=False)
    age = models.PositiveIntegerField(blank=False)
    location = models.CharField(max_length=255, blank=True)

    def clean(self):
        if self.gender == self.looking_for:
            raise ValidationError('You cannot look for the same gender as yourself.')

    def __str__(self):
        return f"{self.name} ({self.gender}) - {self.age} years old, Looking for {self.looking_for}, Located in {self.location}"
