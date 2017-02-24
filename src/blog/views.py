from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.shortcuts import get_object_or_404


def posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts':posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {'post':post})

