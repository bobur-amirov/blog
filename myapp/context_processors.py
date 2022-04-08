from .models import Category, Tag, Blog


def category(request):
    categories = Category.objects.all()

    return {'categories': categories}


def tag(request):
    tags = Tag.objects.all()

    return {'tags': tags}


def top_blogs(request):
    top_blogs = Blog.objects.all().order_by('-views')[:5]

    return {'top_blogs': top_blogs}
