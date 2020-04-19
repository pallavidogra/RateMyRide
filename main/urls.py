from django.urls import path
from .views import (
        PostDetailView,
        PostCreateView,
        PostUpdateView
    )
from . import views

urlpatterns = [
    path('', views.home, name='main_view'),
    path('post_detail/<int:pk>/', views.PostDetailView, name='post-detail'),
    path('post/new/', PostCreateView, name='post-create'),
    path('post/5/update', PostUpdateView, name='post-update'),
    path('about/', views.about, name='main_about'),
    path('my_post/', views.my_post, name='my-post'),
    path('add_rating/', views.add_rating, name='add-rating'),
    path('add_comment/', views.add_comment, name='add-comment'),
    path('get_rating/', views.get_rating, name='get-rating'),
    path('post_details/', views.post_detail, name='post-details'),
    path('post-modal/', views.modal, name='post_modal'),
 ]