from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import role, Teacher, SP,constore, Suggestions, POST
from django.contrib import messages
from django.contrib.sessions import *
import random
# Create your views here.
def studhome(request):
	given = Suggestions.objects.all()
	posts = POST.objects.all()
	return render(request,'heads.html',{'givens':given,'posts':posts})

def teacher_dash(request):
	if 'eyobed' in request.session:
		suggestions = Suggestions.objects.filter(suggestion_for='teacher',given_for=request.session['eyobed'])
		poster_id = request.session['eyobed']
		return render(request,'teachersdashboard.html',{'suggestions':suggestions,'poster_id':poster_id})
	else:
		messages.info(request,'login first')
		return redirect('login')	
def service_provider_dash(request):
	if 'eyobed' in request.session:
		suggestions = Suggestions.objects.filter(suggestion_for='service provider',given_for=request.session['eyobed'])
		return render(request,'service_provider_dash.html',{'suggestions':suggestions})
	else:
		messages.info(request,'login first')
		return redirect('login')
def add_suggestion(request):
	if request.method == 'GET':
		suggest_for = request.GET['suggestion']
def give_suggestion(request):
	if request.method == 'POST':
		given_for = request.POST['service']
		overall = request.POST['overall']
		suggestion = request.POST['suggestion']
		typ = request.POST['typ']

		suggest = Suggestions(given_for = given_for,overall=overall,idea=suggestion,suggestion_for=typ)
		suggest.save()
		messages.info(request,'succesfully given')
		if typ == 'service provider':
			return redirect('forsp')
		elif typ == 'teacher':
			return redirect('forteacher')
	else:
		return redirect('forsp')

def suggestions(request):
	givens = Suggestions.objects.all()
	return render(request,'suggestions.html',{'givens':givens})
