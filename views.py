from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import role, Teacher, SP,constore, Suggestions, POST
from django.contrib import messages
from django.contrib.sessions import *
from django.core.mail import send_mail
import random
from django.conf import settings
# Create your views here.
def studhome(request):
def adminhome(request):
	return render(request,'header.html')
def registerT(request):
def accsp(request):
def requestFRSP(request):
def all(request):
	return render(request,'all.html')
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)
		if user is not None:
			rl = role.objects.get(username=user.username)
			if rl.role == 'admin':
				auth.login(request,user)
				return redirect('adminhome')
			elif rl.role == 'teacher':
				auth.login(request,user)
				tid = Teacher.objects.get(email=user.email).id
				request.session['malda'] = tid
				request.session['user_id'] = user.id
				return redirect('teacher_dash')
			elif rl.role == 'service provider':
				auth.login(request,user)
				sid = SP.objects.get(email=user.email).id
				request.session['malda'] = sid
				request.session['user_id'] = user.id
				return redirect('service_provider_dash')
			else:
				return redirect('all')
		else:
			messages.info(request,'incorrect credential')
			return redirect('login')
	else:
		return render(request,'login.html')
def confirm(request):
def sg(request):
def logout(request):
def forteacher(request):
def forsp(request):
def dash(request):
	return render(request,'board.html')
def signup_form(request):
def teacher_dash(request):
def service_provider_dash(request):
def add_suggestion(request):
def give_suggestion(request):
def post(request):
def service_provider_post(request):
def suggestions(request):
def posts(request):
