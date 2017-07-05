from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

SUBJECTSf =  (
	('Skill Development Lab','SDL'),
	('Computer Networks','CN'),
	('Theory of Computation','TOC'),
	('Database Management Systems','DBMS'),
	('Information System and Engineering Economics','IS & EE'),
	('Software Engineering and Project Management','SE & PM')
)

SUBJECTSs = (
	('sdlt','SDL'),
	('cn','CN'),
	('toc','TOC'),
	('dbms','DBMS'),
	('is&ee','IS & EE'),
	('se&pm','SE & PM'),
	('sdl','SDL Lab'),
	('dbmsl','DBMS Lab'),
	('cnl','CN Lab')
)

CLASSES = (
#	('SEA','SE A'),
#	('SEB','SE B'),
#	('SEC','SE C'),
	('TEA','TE A'),
	('TEB','TE B'),
	('TEC','TE C'),
#	('BEA','BE A'),
#	('BEB','BE B'),
#	('BEC','BE C')
)

NUMBERS = [ (i,i) for i in range(1,len(SUBJECTSf)+1) ]

class SignUpForm(UserCreationForm):
	teacher_name = forms.CharField(max_length=50, help_text='Enter your full name')
	#last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254,  required=False, help_text='Optional. Inform a valid email address.')
	no_of_subjects=forms.ChoiceField(choices=NUMBERS,required=True,help_text='Number of subjects taught by you')
	subjects = forms.ChoiceField(choices=SUBJECTSf,required=True, help_text='Subject taught by you')

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
	div = forms.ChoiceField(choices=CLASSES,required=True)
	subj = forms.ChoiceField(choices=SUBJECTSs,required=True)
	absent_list = forms.CharField(required=True,help_text='Enter roll numbers of absent students separated by space')
