from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post

# Create your views here.


class HomeView(ListView):
    model = Post
    context_object_name = 'blog_list'
    template_name = 'home.html'
