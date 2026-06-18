from django.db import models
from django.contrib.auth.models import User
USER_TYPES = [
    ('student', 'Student'),
    ('teacher', 'Teacher'),
    ('admin', 'Admin'),
    ('librarian', 'Librarian'),
]
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='student')
    def __str__(self):
        return f"{self.user.username}'s profile"