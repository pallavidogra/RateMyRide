from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView
    )
from .models import Post
from .forms import postUpdateForm



def home(request):
    dictContext = {
        'keyPosts': Post.objects.all()
    }

    return render(request,'main/home.html', dictContext)


class PostListView(ListView):
    model = Post

    # defaults to: <app>/<model>_<viewtype>.html
    template_name = 'main/home.html'

    context_object_name = 'keyPosts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

    # defaults to: <app>/<model>_<viewtype>.html
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post

    # url defaults to: <app>/<model>_<viewtype>.html

    fields = ['title', 'imgRide', 'description']
    #fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
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