from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


class HomeView(ListView):
    model = Post
    context_object_name = 'blog_list'
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    # context_object_name = 'detail_view'
    template_name = 'post_detail.html'
