from django.forms import ModelForm
from .models import Blog

class BlogForm(ModelForm):
	model = Blog
	addblog = ('title', 'text',)