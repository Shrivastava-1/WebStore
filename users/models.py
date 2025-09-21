from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    gender_options = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Not Prefer', 'Not Prefer')
    ]
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255, choices=gender_options, blank=True)
    image = models.ImageField(upload_to='profile/', default='profile.jpg', blank=True)

    def save(self, *args, **kwargs):
        if not self.gender:
            self.gender = 'None'
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name}"