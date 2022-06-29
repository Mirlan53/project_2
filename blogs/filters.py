import django_filters
from .models import Blog, Tag, CAT_CHOICES

# class BlogFilter(django_filters.FilterSet):
# 	class Meta:
# 		model = Blog
# 		fields = ('title', 'text')

# class BlogFilter(django_filters.FilterSet):
# 	class Meta:
# 		model = Blog
# 		fields = {
# 			'title': ['icontains'],
# 			'text': ['icontains']
# 		}


class BlogFilter(django_filters.FilterSet):
	category = django_filters.ChoiceFilter(choices=CAT_CHOICES)

	class Meta:
		model = Blog
		fields = []