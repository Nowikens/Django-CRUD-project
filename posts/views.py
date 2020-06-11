from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm
# Create your views here.

@login_required
def index(request):
    posts = Post.objects.all().order_by('-date_posted')
    form = PostForm()
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts:index')
    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'posts/index.html', context)

@login_required
def update_post(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(instance=post)
    if request.method == "POST":
        updated_post = PostForm(request.POST, instance=post)
        updated_post.save()
        return redirect('posts:index')
    context = {
        'post': post,
        'form': form
    }
    return render(request, 'posts/update.html', context)

@login_required
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    
    post.delete()
    return redirect('posts:index')
    
    
    
    
    
    
    
    
    
    
    