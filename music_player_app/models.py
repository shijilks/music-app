# music_player_app/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields here
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    # Define custom related names for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',  # Custom related name for groups
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',  # Custom related name for user_permissions
        related_query_name='custom_user'
    )

    def __str__(self):
        return self.username
