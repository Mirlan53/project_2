from django.shortcuts import render
from .models import Blog, Book

def blog_list(request):
	blogs = Blog.objects.all() # Запрашиваем из БД все блоги
	context = {
		'blogs': blogs,
	}
	return render(request, 'blogs/blog_list.html', context)


def book(request):
	blogs = Blog.objects.all() # Запрашиваем из БД все блоги
	context = {
		'blogs': blogs,
	}
	return render(request, 'blogs/book.html', context)