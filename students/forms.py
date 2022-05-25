from django.forms import ModelForm
from students.models import Student, Teacher

class StudentForm(ModelForm):
	class Meta:
		model = Student
		# fields = '__all__'
		fields = (
			'name', 'surname', 'birth_date', 'school', 'grade', 'average_mark'
		)

class TeacherForm(ModelForm):
	class Meta:
		model = Teacher
		# fields = '__all__'
		fields = (
			'name', 'birth_date'
		)