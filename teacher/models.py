
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Teacher(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	teacher_name = models.TextField(max_length = 250)
	#teacher_username = models.CharField(max_length = 250)
    #bio = models.TextField(max_length=500, blank=True)
    #location = models.CharField(max_length=30, blank=True)
    #birth_date = models.DateField(null=True, blank=True)
	subjects = models.CharField(max_length=250, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Teacher.objects.create(user=instance)
	print(dir(instance))
	instance.teacher.save()