from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_details(request,num):
    post = Post.objects.filter(pk=num)
    return render(request, 'blog/post_details.html', {'post': post})
