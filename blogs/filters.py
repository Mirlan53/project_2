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
	category = django_filters.ChoiceFilter(empty_label="выберите категорию", choices=CAT_CHOICES)
	title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='по загаловку')
	tags = django_filters.ModelMultipleChoiceFilter(label="тег", field_name="tags", queryset=Tag.objects.all())
	# tags = django_filters.ModelChoiceFilter(label="тег", empty_label="выберите тег", field_name="tags", queryset=Tag.objects.all())