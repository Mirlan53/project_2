from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Teacher
from .forms import StudentForm, TeacherForm

def student_list(request): 
	students = Student.objects.all()
	context = {
		'students': students
	}
	return render(request, 'students/student_list.html', context)

def student_detail(request, student_id):
	# student = Student.objects.get(id = student_id)
	student = get_object_or_404(Student, id=student_id)
	context = {
		'student': student
	}
	return render(request, 'students/student_detail.html', context)

def student_create(request):
	form = StudentForm(request.POST or None, files=request.FILES)
	if request.method == 'POST':
		if form.is_valid:
			form.save()
			return redirect('student_list')

	context = {
	'form': form
	}
	return render(request, 'students/student_create.html', context)

def teacher_create(request):
	form = StudentForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid:
			form.save()
			return redirect(student_list)
	
	context = {
		'form': form
		}
	return render(request, 'students/teacher_create.html', context)

def student_update(request, student_id):
	student = get_object_or_404(Student, id=student_id)
	form = StudentForm(request.POST or None, instance=student)
	if request.method == 'POST':
		if form.is_valid:
			form.save()
			return redirect(student_list)
	
	context = {
			'form': form
			}
	return render(request, 'students/student_update.html', context)
	
def student_delete(request, student_id):
	student = get_object_or_404(Student, id=student_id)
	# Берем ученика из БД
	if request.method == 'POST':
		student.delete()
		return redirect(student_list)

	context = {
		'student': student
	}
	return render(request, 'students/student_delete.html', context)


def teachers_students(request, teacher_id):
	students = Student.objects.filter(teacher_id = teacher_id)
	teachers = Teacher.objects.all()
	context = {
			'students': students,
			'teachers': teacher
	}

	return render(request, 'students/student_list.html', context)
