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
  description = models.TextField(blank=True,null=True)
  date_posted = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk})

  class Meta:
    db_table='post'

    
class Rating(models.Model):
  post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='review')
  pub_date = models.DateTimeField(default=timezone.now)
  comment = models.CharField(max_length=200,blank=True,null=True)
  rating = models.IntegerField(default=0)

  def __str__(self):
    return str(self.post)

  class Meta:
    db_table ='post_rating'

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ["created_on"]
#         db_table = 'post_comments'

#     def __str__(self):
#         return "Comment {} by {}".format(self.body, self.name)

