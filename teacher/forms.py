from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	teacher_name = forms.CharField(max_length=50, help_text='Enter your full name')
	#last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254,  required=False, help_text='Optional. Inform a valid email address.')
	subjects = forms.CharField(max_length=150, help_text='Subjects to be taught by you. Add subjects separated by a comma " "')

	class Meta:
		model = User
		fields = ('username', 'teacher_name' , 'email', 'subjects', 'password1', 'password2', )