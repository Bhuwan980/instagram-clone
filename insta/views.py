from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Post
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django import forms

# Create your views here.

class Authorlistview(ListView):
    template_name = 'list_view.html'
    model = Post
    context_object_name = 'posts'
class Authordetailview(DetailView):
    template_name = 'detail.html'
    model = Post
    context_object_name = 'posts'

class createpost(CreateView):
    model = Post
    context_object_name = "posts"
    template_name = 'insta/create.html'
    fields = ['author','image','caption']
    success_url = '/'  