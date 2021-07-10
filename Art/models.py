from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class artWork (models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    Price = models.FloatField()
    image = models.ImageField()
    date_posted = models.DateTimeField(default=timezone.now)
    creator_email = models.TextField(default='#')

    def get_absolute_url(self):
        return reverse('artwork-home')