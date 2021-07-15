from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class artWork (models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    Price = models.DecimalField(max_digits=4,decimal_places=2)
    image = models.ImageField()
    date_posted = models.DateTimeField(default=timezone.now)
    creator_email = models.TextField(default='')

    def get_absolute_url(self):
        return reverse('artwork-home')

class suggestArt(models.Model):
    title = models.CharField(max_length=100)
    suggestion = models.TextField(default='')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('artwork-home')

class reportArt(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(default='')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('artwork-home')