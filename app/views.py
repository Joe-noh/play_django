from django.shortcuts import render, redirect
from app.models import Post

def index(request):
    posts = Post.objects.order_by('-created_at')
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

def new(request):
    if request.method == 'POST':
        post = Post(content = request.POST['content'])
        post.save()

        return redirect('index')
    else:
        return render(request, 'new.html')
