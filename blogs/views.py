from django.shortcuts import render
from .models import Blog, Book

def blog_list(request):
	blogs = Blog.objects.all() # Запрашиваем из БД все блоги
	context = {
		'blogs': blogs,
	}
	return render(request, 'blogs/blog_list.html', context)


def book_list(request):
	books = Book.objects.all() # Запрашиваем из БД все блоги
	context = {
		'books': books,
	}
	return render(request, 'blogs/book_list.html', context)