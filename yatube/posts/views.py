from django.shortcuts import render, get_object_or_404
from .models import Post, Group

POST_COUNT = 10


def index(request):
    posts = Post.objects.all()[:POST_COUNT]
    context = {
        'posts': posts,
    }
    template = 'posts/index.html'
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POST_COUNT]
    context = {
        'group': group,
        'posts': posts,
    }
    template = 'posts/group_list.html'
    return render(request, template, context)
