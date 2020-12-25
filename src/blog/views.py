from django.shortcuts import render, get_object_or_404
from .models import Post


def blog_home(request):
    posts = Post.objects.all().order_by('-created')[:5]
    return render(request, 'blog/blog_home.html', {'posts': posts})


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_details.html', {'post': post})
