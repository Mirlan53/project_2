from django.contrib import admin
from .models import Blog, Book, Tag

admin.site.register(Blog)
admin.site.register(Book)
admin.site.register(Tag)