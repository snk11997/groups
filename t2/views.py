from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm, UserRegistrationForm

def index(request):
    posts = BlogPost.objects.all()
    return render(request, 't2/index.html', {'posts': posts})

def view_post(request, id):
    post = get_object_or_404(BlogPost, pk=id)
    return render(request, 't2/view_post.html', {'post': post})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # # print(post.author, "post.author start")
            post.author = request.user
            # print(post.author, "post.author")
            # print(request.user, "request.user")
            post.save()
            return redirect('index')
    else:
        form = BlogPostForm()
    return render(request, 't2/post_form.html', {'form': form})

@login_required
def edit_post(request, id):
    post = get_object_or_404(BlogPost, id=id, author=request.user)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 't2/post_form.html', {'form': form})

@login_required
def delete_post(request, id):
    post = get_object_or_404(BlogPost, id=id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 't2/confirm_delete.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 't2/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 't2/login.html', {'error': 'Invalid credentials'})
    return render(request, 't2/login.html')

def user_logout(request):
    logout(request)
    return redirect('index')
