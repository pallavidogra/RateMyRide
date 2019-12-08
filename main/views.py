from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView
    )
from .models import Post
from .forms import postUpdateForm, PostCreateForm



def home(request):
    current_user = str(request.user)
    filter_user = Post.objects.filter(author__username__iexact=current_user)
    Context = {
        'keyPosts': filter_user
    }

    return render(request,'main/home.html', Context)


# class PostListView(ListView):
#     model = Post

#     # defaults to: <app>/<model>_<viewtype>.html
#     template_name = 'main/home.html'

#     context_object_name = 'keyPosts'
#     ordering = ['-date_posted']


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
        



def about(request):
    return render(request,'main/about.html', {'title': 'About'})