from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator

from .models import Blog, Category, Tag
from .forms import RegisterForm, BlogForm, CommentForm


def home(request):
    blogs = Blog.objects.all()

    paginator = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'blogs': page_obj,
    }

    return render(request, 'home.html', context)


def category_list(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'category_list.html', context)


def category_blogs(request, slug):
    category = Category.objects.get(slug=slug)
    blogs = Blog.objects.filter(category=category)

    context = {
        'category': category,
        'blogs': blogs
    }

    return render(request, 'category_blogs.html', context)


def tag_blogs(request, slug):
    tag = Tag.objects.get(slug=slug)
    blogs = Blog.objects.filter(tags=tag)

    context = {
        'tag': tag,
        'blogs': blogs,
    }

    return render(request, 'tag_blogs.html', context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form_commnet = form.save(commit=False)
            form_commnet.blog = blog
            form_commnet.user = request.user
            form_commnet.save()
            return redirect('blog_detail', blog.slug)
    else:
        form = CommentForm()

    blog.views += 1
    blog.save()

    context = {
        'blog': blog,
        'form': form,
    }

    return render(request, 'blog_detail.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, 'register.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username yoki password xato!')
            return redirect('login_page')

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login_page')
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES or None)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.slug = slugify(form2.title)
            form2.user = request.user
            form2.save()
            blog = Blog.objects.get(id=form2.id)
            tags_req = form.cleaned_data.get('tags')
            tag_list = list(tags_req.split(','))
            for t in tag_list:
                t, created = Tag.objects.get_or_create(name=t.strip())
                blog.tags.add(t)
            return redirect('home')
    else:
        form = BlogForm()

    context = {
        'form': form
    }

    return render(request, 'blog_create.html', context)


def blog_update(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    form = BlogForm(request.POST or None, instance = blog)
    if form.is_valid():
        form2 = form.save(commit=False)
        form2.slug = slugify(form2.title)
        form2.save()
        tags_req = form.cleaned_data.get('tags')
        tag_list = list(tags_req.split(','))
        for t in tag_list:
            t, created = Tag.objects.get_or_create(name=t.strip())
            blog.tags.add(t)
        return redirect('blog_detail', blog.slug)

    context = {
        'blog': blog,
        'form': form,
    }

    return render(request, 'blog_update.html', context)


def blog_delete(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')

    context = {
        'blog':blog
    }

    return render(request, 'blog_delete.html', context)


def user_list(request):
    users = User.objects.all()

    context = {
        'users': users
    }

    return render(request, 'user_list.html', context)