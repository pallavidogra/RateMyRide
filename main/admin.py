from django.contrib import admin
from .models import Post, Rating

# Register your models here.
admin.site.register(Rating)
admin.site.register(Post)