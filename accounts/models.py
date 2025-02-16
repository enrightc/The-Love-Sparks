from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
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

    FREE_TIME_CHOICES = [
        ('creative', 'Creative hobbies (painting, music, etc.)'),
        ('active', 'Staying active (Sports, hiking, working out)'),
        ('learning', 'Learning and discovery (reading, puzzles, documentaries)'),
        ('social', 'Socialising and entertainment (movies, concerts, parties)'),
    ]

    FRIENDS_DESCRIPTION_CHOICES = [
        ('outgoing', 'Outgoing and energetic'),
        ('thoughtful', 'Thoughtful and analytical'),
        ('caring', 'Caring and empathic'),
        ('ambitious', 'Ambitious and determined'),
    ]

    RELATIONSHIP_EXCITEMENT_CHOICES = [
        ('experiences', 'Exploring new experiences together'),
        ('deep_connection', 'Deep conversations and emotional connection'),
        ('humour', 'Sharing humour and lighthearted fun'),
        ('stability', 'Building a comfortable and stable life together'),
    ]

    email = models.EmailField(unique=True, blank=False)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, blank=False)
    looking_for = models.CharField(max_length=50, choices=LOOKING_FOR_CHOICES, blank=False)
    age = models.IntegerField(null=True, blank=True)

    free_time_preference = models.CharField(max_length=50, choices=FREE_TIME_CHOICES, blank=False)
    friends_description = models.CharField(max_length=50, choices=FRIENDS_DESCRIPTION_CHOICES, blank=False)
    relationship_excites = models.CharField(max_length=50, choices=RELATIONSHIP_EXCITEMENT_CHOICES, blank=False)

    