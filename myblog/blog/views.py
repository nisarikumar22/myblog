from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    all_post = Post.objects.all()
    context = {
        'posts' : all_post
    }
    return render(request, 'blog/home.html', context)