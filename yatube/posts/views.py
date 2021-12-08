from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from .models import Group, Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm


@login_required
def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': page_obj
    }
    return render(request, template, context)


@login_required
def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'posts': page_obj,
    }
    return render(request, template, context)


@login_required
def profile(request, username):
    context = {
    }
    return render(request, 'posts/profile.html', context)


@login_required
def post_detail(request, post_id):
    context = {
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/profile/<username>/')
        return render(request, 'posts/create_post.html', {'form': form})
    form = PostForm()
    is_edit = True
    return render(request, 'posts/create_post.html', {'form': form, 'is_edit': is_edit})


@login_required
def post_edit(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/profile/<username>/')
        return render(request, 'posts/create_post.html', {'form': form})
    form = PostForm()
    is_edit = False
    return render(request, 'posts/create_post.html', {'form': form, 'is_edit': is_edit})
