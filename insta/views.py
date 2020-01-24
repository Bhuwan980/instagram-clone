from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Post

# Create your views here.

class Authorlistview(ListView):
    template_name = 'list_view.html'
    model = Post
    context_object_name = 'posts'
class Authordetailview(DetailView):
    template_name = 'detail.html'
    model = Post
    context_object_name = 'posts'