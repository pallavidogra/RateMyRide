from django.contrib import admin
from .models import Post, Review

# Register your models here.
admin.site.register(Review)
admin.site.register(Post)