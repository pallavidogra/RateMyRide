from django.urls import path
from .views import (
        PostListView,
        PostDetailView,
        PostCreateView,
        PostUpdateView
    )
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='main_view'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/5/update', PostUpdateView, name='post-update'),
    path('about/', views.about, name='main_about'),


 ]

 