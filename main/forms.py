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
from .models import Post

        
class postUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['imgRide']