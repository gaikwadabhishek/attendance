from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

SUBJECTS =  (
	('Skill Development Lab','SDL'),
	('Computer Networks','CN'),
	('Theory of Computation','TOC'),
	('Database Management Systems','DBMS'),
	('Information System and Engineering Economics','IS & EE'),
	('Software Engineering and Project Management','SE & PM')
)

NUMBERS = [ (i,i) for i in range(1,len(SUBJECTS)+1) ]

class SignUpForm(UserCreationForm):
	teacher_name = forms.CharField(max_length=50, help_text='Enter your full name')
	#last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254,  required=False, help_text='Optional. Inform a valid email address.')
	no_of_subjects=forms.ChoiceField(choices=NUMBERS,required=True,help_text='Number of subjects taught by you')
	subjects = forms.ChoiceField(choices=SUBJECTS,required=True, help_text='Subject taught by you')

	class Meta:
		model = User
		fields = ('username', 'teacher_name' , 'email', 'subjects', 'password1', 'password2', )
		widgets = {
			'username': forms.TextInput(),
			'teacher_name':forms.TextInput(),
			'email':forms.TextInput(),
			'password1':forms.TextInput(),
			'password2':forms.TextInput()
		}

class AbsentForm(forms.Form):
	absent_list = forms.CharField(help_text='Enter roll numbers of absent students separated by space')
