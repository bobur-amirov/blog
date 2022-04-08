from django.contrib import admin

from .models import Category, Tag, Blog, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'user', 'created', 'views']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category', 'tags']
    search_fields = ['title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'blog', 'user', 'created']
    list_filter = ['blog', 'user']
    search_fields = ['text']