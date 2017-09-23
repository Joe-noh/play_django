from django.shortcuts import render
from app.models import Post

def index(request):
    posts = Post.objects.order_by('-created_at')
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)
