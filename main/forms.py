# forms.py extens form to include an email address

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  UpdateView
    )
from .models import Post,Rating

class postUpdateForm(forms.ModelForm):
    
  class Meta:
    model = Post
    fields = ['imgRide']


class PostCreateForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = '__all__'
    exclude = ['author', 'date_posted']


class PostComment(forms.ModelForm):
  class Meta:
    model = Rating
    fields = ['comment']

    widgets= {
      'comment': forms.TextInput(attrs={'class': 'form-control'}),
    }        

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name', 'email', 'body')