
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

SUBJECTS =  (
	('Skill Development Lab','SDL'),
	('Computer Networks','CN'),
	('Theory of Computation','TOC'),
	('Database Management Systems','DBMS'),
	('Information System and Engineering Economics','IS & EE'),
	('Software Engineering and Project Management','SE & PM')
)

class Teacher(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	teacher_name = models.TextField(max_length = 250)
	#teacher_username = models.CharField(max_length = 250)
    #bio = models.TextField(max_length=500, blank=True)
    #location = models.CharField(max_length=30, blank=True)
    #birth_date = models.DateField(null=True, blank=True)
	subjects = models.CharField(max_length=7, choices=SUBJECTS)
	
	def __str__(self):
		return self.teacher_name


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Teacher.objects.create(user=instance)
	instance.teacher.save()
	
class Subject(models.Model):
	subject_teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
	subject_name = models.CharField(max_length = 50)
	#how many lectures in a week?
	subject_count = models.IntegerField(blank = False)
	
	def __str__(self):
		return self.subject_name