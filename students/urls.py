from django.urls import path
from .views import student_list, student_detail, student_create, teacher_create, student_update, student_delete

urlpatterns = [
	path('students', student_list, name='student_list'),
	path('students/<int:student_id>', student_detail, name='student_detail'),
	path('student_create', student_create, name='student_create'),
	path('teacher_create', teacher_create, name='teacher_create'),
	path('student_update/<int:student_id>', student_update, name='student_update'),
	path('student_delete/<int:student_id>', student_delete, name='student_delete'),
]