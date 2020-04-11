from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Post, Rating, Comment
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
    )
from .forms import (
        postUpdateForm, 
        PostCreateForm,
        PostComment,
        CommentForm
    )
from django.utils import timezone


def home(request):
    all_posts = Post.objects.all().order_by('-id')
    rating = Rating.objects.filter()
    comment = request.POST.get('post_comment')
    if request.method == 'POST':
        form = PostComment(request.POST)
        if form.is_valid():
            form.save()
        return redirect('main_view')
    else:
        form = PostComment()

    context = {
        'keyPosts': all_posts,
        'form':form
    }

    return render(request,'main/home.html', context)

def my_post(request):
    current_user = str(request.user)
    filtered_posts = Post.objects.filter(author__username__iexact=current_user)

    context = {
        'keyPosts': filtered_posts
    }

    return render(request,'main/home.html', context)

class PostDetailView(DetailView):
    model = Post

    # defaults to: <app>/<model>_<viewtype>.html

def PostCreateView(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form_post  = form.save(commit=False)
            form_post.author = request.user
            form_post.save()
        return redirect('main_view')
    else:
        form = PostCreateForm()

    return render(request, "main/post_form.html", {'form': form })


def PostUpdateView(request):

    if request.method == 'POST':
        form = postUpdateForm(request.POST or None, request.FILES or None )

        def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)
    else:
        model = Post
        
        # url defaults to: <app>/<model>_<viewtype>.html

        fields = ['title', 'imgRide', 'description']
        #fields = ['title', 'description']
        #return render(request, 'users/profile.html', context)
        
        def form_valid(self, form):
            form.instance.author = self.request.user
            #return super().form_valid(form)
        return render(request, 'main/form_update.html')
        
@login_required
def add_rating(request):
    rating  = request.POST.get("rating")
    updated_rating = None
    post_id  = request.POST.get("post_id")
    post_obj = Post.objects.get(id=post_id)
    try:
        review_obj = post_obj.review
        review_obj.rating = rating
        review_obj.save()
        updated_rating = post_obj.review.rating
    except:
        review_obj = Rating.objects.create(
            post=post_obj,
            rating=rating,
            pub_date=timezone.now()
        )
        updated_rating = review_obj.rating
    if not updated_rating:
        return JsonResponse({'error': True})
    return JsonResponse({'error': False, 'rating':rating})

@login_required
def add_comment(request):
    post_id  = request.POST.get("post_id")
    post_obj = Post.objects.get(id=post_id)
    post_comment = request.POST.get("comment")
    if post_comment:    
        review_obj = post_obj.review
        review_obj.comment = post_comment
        review_obj.save()
    return JsonResponse({'error': False})

def post_detail(request):
    template_name = "main/post_detail.html"
    post = get_object_or_404(Post)
    # comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            # "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )

def get_rating(request):
    post_id  = request.POST.get("post_id")
    try:
        post_obj = Post.objects.get(id=post_id)
    except:
        post_obj = None
    if post_obj:
        review_obj = post_obj.review
        rating = review_obj.rating
        comment = review_obj.comment 
        return JsonResponse({'error': False, 'rating':rating, 'comment':comment})
    else:
        return JsonResponse({'error': True})

def about(request):
    return render(request,'main/about.html', {'title': 'About'})