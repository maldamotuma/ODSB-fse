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
def registerT(request):
def accsp(request):
def requestFRSP(request):
def all(request):
def login(request):
def confirm(request):
def sg(request):
def logout(request):
	auth.logout(request)
	messages.info(request,'you logged out successfully')
	return redirect('login')
def forteacher(request):
def forsp(request):
def dash(request):
def signup_form(request)
def teacher_dash(request):
def service_provider_dash(request):
def add_suggestion(request):
def give_suggestion(request):
def post(request):
def service_provider_post(request):
def suggestions(request):
def posts(request):
	
