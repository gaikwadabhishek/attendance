# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Teacher(models.Model):
	teacher_name = models.CharField(max_length = 250)
	teacher_username = models.CharField(max_length = 250)
	def __str__(self):
		return self.teacher_name