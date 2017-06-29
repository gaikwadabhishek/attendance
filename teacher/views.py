# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse            #http response sends back html/basic webpage
from django.conf.urls import include
from django.template import loader
from .models import Teacher
from django.http import Http404
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
# Create your views here.
def index(request):
    all_objects = Teacher.objects.all()
    html = ''
    for teacher in all_objects:
        url = "/teacher/" + str(teacher.teacher_username) + "/"
        html += '<a href = "' + url + '">' +  teacher.teacher_name + '</a><br>'
    return HttpResponse(html)

def detail(request, teacher_username):
		try:
			teacher_id = Teacher.objects.get(pk=album_id)
		except Teacher.DoesNotExist:
			raise Http404("Teacher Does Not Exist! ")
			



def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})