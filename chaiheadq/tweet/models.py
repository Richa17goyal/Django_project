from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Corrected 'User'
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Corrected 'created_add' to 'created_at'
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # Fixed syntax for __str__ method
        return f'{self.user.username} - {self.text[:10]}'
