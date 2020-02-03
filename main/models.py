from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    imgRide = models.ImageField(upload_to='rate-my-ride', blank=True)
    imgRide.verbose_name = "Your Ride"
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    
class Review(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='review')
    pub_date = models.DateTimeField()
    comment = models.CharField(max_length=200)
    rating = models.IntegerField()


