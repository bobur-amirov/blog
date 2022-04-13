from django.urls import path

from .views import (home, category_list, category_blogs,
                    tag_blogs, blog_detail, login_page, logout_page,
                    register, blog_create, blog_update, blog_delete, user_list)

urlpatterns = [
    path('', home, name='home'),
    path('categories/', category_list, name='category_list'),
    path('category/<slug:slug>', category_blogs, name='category_blogs'),
    path('tag/<slug:slug>', tag_blogs, name='tag_blogs'),
    path('blog/<slug:slug>', blog_detail, name='blog_detail'),
    path('register', register, name='register'),
    path('login', login_page, name='login_page'),
    path('logout', logout_page, name='logout_page'),
    path('create/', blog_create, name='blog_create'),
    path('update/<slug:slug>', blog_update, name='blog_update'),
    path('delete/<slug:slug>', blog_delete, name='blog_delete'),
    path('users', user_list, name='user_list'),
]