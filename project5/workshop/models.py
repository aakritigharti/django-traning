

# Create your models here.
from django.db import models

# models.py

class Workshop(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    workshops = models.ManyToManyField(Workshop, blank=True)

    def __str__(self):
        return self.name
