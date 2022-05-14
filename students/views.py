from django.shortcuts import render
from .models import Student

def student_list(request): 
	students = Student.objects.all()
	context = {
		'students': students
	}
	return render(request, 'blogs/student_list.html', context)

def student_detail(request, student_id):
	student = Student.objects.get(id = student_id)
	context = {
		'student': student
	}
	return render(request, 'blogs/student_detail.html', context)