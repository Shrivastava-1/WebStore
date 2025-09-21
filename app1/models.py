import os
from django.db import models

class Description(models.Model):
    scientific_name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    nutrition = models.TextField(blank=True)
    benefits = models.TextField(blank=True)
    usage = models.TextField(blank=True)
    season = models.CharField(max_length=100, blank=True)
    origin = models.CharField(max_length=100, blank=True)
    fun_facts = models.CharField(max_length=150, blank=True)

    def save(self, *args, **kwargs):
        if not self.scientific_name:
            self.scientific_name = "Name"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.scientific_name


def upload(instance, filename):
    return os.path.join(instance.field, filename)


class Allitems(models.Model):
    FIELD_CHOICES = [
        ('food', 'food'),
        ('vegetable', 'vegetable'),
        ('dairy', 'dairy'),
        ('meat', 'meat'),
        ('mens', 'mens'),
        ('womens', 'womens'),
        ('kids', 'kids'),
    ]

    name = models.CharField(max_length=255, blank=True)
    rate = models.IntegerField(blank=True, null=True)
    field = models.CharField(max_length=255, choices=FIELD_CHOICES, blank=True)
    quality = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to=upload, default='image.jpg', blank=True)

    def save(self, *args, **kwargs):
        if not self.quality:
            self.quality = "Good"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}"