from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Extended user model with avatar support."""
    name   = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio    = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.username

    def get_display_name(self):
        return self.name or self.username