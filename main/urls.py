from django.urls import path
from .views import (
        PostDetailView,
        PostCreateView,
        PostUpdateView
    )
from . import views

urlpatterns = [
    path('', views.home, name='main_view'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView, name='post-create'),
    path('post/5/update', PostUpdateView, name='post-update'),
    path('about/', views.about, name='main_about'),
    path('my_post/', views.my_post, name='my-post'),
 ]