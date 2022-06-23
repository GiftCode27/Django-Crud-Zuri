from django.shortcuts import render
from django_urls import reverse_lazy
from django_views import generic
from .models import post
# Create your views here.


class PostListView(generic.listview):
  model=post

class PostCreateView(generic.createview):
  model=post
  fields="__all__"
success_url=reverse_lazy("blog:all")

class PostDetailView(generic.detailview):
  model=post

class PostUpdateView(generic.updateview):
   model=post
   fields="__all__"
   success_url=reverse_lazy("blog:all")

class PostDeleteView(generic.deleteview):
  model=post
  fields="__all__"
  success_url=reverse_lazy("blog:all")
  
  

  