from django.db import models
from django.conf import settings

class Teacher(models.Model):
	name = models.CharField(max_length=50, unique=True)
	birth_date = models.DateField()

	def __str__(self):
			return self.name

class Student(models.Model):
	name = models.CharField(max_length=50, unique=True)
	surname = models.CharField(max_length=100, unique=True)
	birth_date = models.DateField()
	school = models.CharField(max_length=150, unique=True)
	grade = models.IntegerField()
	average_mark = models.DecimalField(max_digits=2, decimal_places=1)
	photo = models.ImageField(upload_to='student_photos', null=True, blank=True)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

	def __str__(self):
			return f"{self.name}: {self.grade}"