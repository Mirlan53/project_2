from django.shortcuts import render
from .models import Blog, Book
from .forms import BlogForm
from .filters import BlogFilter
from django.core.paginator import Paginator

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

def list_blogs(request):
	blogs = Blog.objects.all()
	page_num = request.GET.get('page')
	paginator = Paginator(blogs, 5)
	blogs = paginator.get_page(page_num)
	context = {
		'blogs': blogs
	}
	if page_num == 1 or page_num is None:
		return render(request, 'page/list_blogs.html', context)
	else:
		return render(request, 'page/list_blogs1.html', context)
	

	return render(request, 'page/list_blogs.html', context)