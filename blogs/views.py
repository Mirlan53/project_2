from django.shortcuts import render
from .models import Blog, Book
from .forms import BlogForm
from .filters import BlogFilter


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

def book_detail(request, book_id):
	book = Book.objects.get(id = book_id)
	context = {
		'book': book
	}
	return render(request, 'blogs/book_detail.html', context)

def blog_create(request):
	form = BlogForm()
	if request.method == 'POST':
		form = BlogForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('blog_list')

	context = {'form': form}
	return render(request, 'blogs/blog_create.html', context)

def blog_filtered(request):
	f = BlogFilter(request.GET, queryset=Blog.objects.all())
	context = {
		'filter': f,
	}
	return render(request, 'blogs/blog_filtered.html', context)