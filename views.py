# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse            #http response sends back html/basic webpage
from django.conf.urls import include
from django.template import loader
from .models import Teacher
from django.http import Http404
from django.contrib.auth.forms import PasswordChangeForm
from .forms import SignUpForm,AbsentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from . import markAttendance
from django.contrib import messages
from django.core.mail import send_mail

def detail(request, teacher_username):
		try:
			teacher_id = Teacher.objects.get(pk=album_id)
		except Teacher.DoesNotExist:
			raise Http404("Teacher Does Not Exist! ")




@login_required
def home(request):
    return render(request, 'home.html')



def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  # load the profile instance created by the signal
            #user.profile.birth_date = form.cleaned_data.get('birth_date')
			user.teacher.teacher_name = form.cleaned_data.get('teacher_name')
			user.teacher.subjects = form.cleaned_data.get('subjects')
			user.refresh_from_db()
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})

@login_required
def change_password(request):
    print ('POST')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            #update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was updated successfully!')  # <-
            return redirect('home')
        else:
            messages.warning(request, 'Please correct the error below.')  
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'teacher/change_password.html', {'form': form})
	
def absentees(request):
	form = AbsentForm()
	if request.method=='POST':
		form = AbsentForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			absents = cd.get('absent_list')
			cl_division = cd.get('div')
			subj = cd.get('subj')
			print('\n'*3 + '*'*20 + '\n'*2)
			print(subj,cl_division,absents)
			print('\n'*2 + '*'*20 + '\n'*3)
			markAttendance.mainWork(absents,subj,cl_division)
	return render(request,'absent.html',{'form':form})
