"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blogs.views import blog_list, book_list, book_detail, blog_create, blog_filtered, list_blogs
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_list, name='blog_list'),
    path('blog_create', blog_create, name='blog_create'),
    path('books', book_list, name='book_list'),
    path('blog_filtered', blog_filtered, name='blog_filtered'),
    path('books/<int:book_id>', book_detail, name='book_detail'),
    path('list_blogs', list_blogs, name='list_blogs'),
    path('', include('students.urls')),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)