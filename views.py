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
	if request.method == 'POST':
		unma = request.POST['uname']
		email = request.POST['email']
		password = request.POST['Password1']
		confirm_password = request.POST['Password2']
		service = request.POST['service']

		if password == confirm_password:
			if User.objects.filter(username = unma ).exists():
				messages.info(request,'username exist use other username')
				return redirect('accsp')
			else:
				if User.objects.filter(email = email).exists():
					messages.info(request,'the same email exists user other email address')
					return redirect('accsp')
				else:
					user = User.objects.create_user(username=unma,email=email,password=password)
					user.save()
					rl = role(username=unma,role="service provider")
					sp = SP(email=email,service=service)
					rl.save()
					sp.save()
					messages.info(request,'successfully created')
					return redirect('accsp')

		else:
			messages.info(request,'password doesnot match')
			return redirect('accsp')
	else:
		return render(request,'createaccforsp.html')
def requestFRSP(request):
def all(request):
	return render(request,'all.html')
def login(request):
def confirm(request):
def sg(request):
def logout(request):
def forteacher(request):
def forsp(request):
	service_providers = SP.objects.all()
	return render(request,'forsp.html',{'service_providers':service_providers})
def dash(request):
	return render(request,'board.html')
