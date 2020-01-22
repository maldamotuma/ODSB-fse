from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import *
from django.contrib import messages
from django.contrib.sessions import *
from django.core.mail import send_mail
import random
from django.conf import settings
# Create your views here.
def studhome(request): #student home or dashboard appeared sfter student login
	if 'email' in request.session:
		given = Suggestions.objects.filter(private='False')
		posts = POST.objects.all()
		giver_id = student.objects.get(email=request.session['email'])
		student_id = giver_id.student_id
		request.session['student_id']=student_id
		return render(request,'heads.html',{'givens':given,'posts':posts})
	else:
		messages.info(request,'Log in first')
		return redirect('login')
def adminhome(request): #admin home page
	return render(request,'header.html')
def registerT(request): #registeres teacher comes on admin page
	if request.method == 'POST':
		first_name = request.POST['fname']
		last_name = request.POST['lname']
		email = request.POST['email']
		department = request.POST['department']

		tchr = Teacher(first_name=first_name,last_name=last_name,email=email,department=department)
		tchr.save()
		messages.info(request,'successfully regitstered')
		return redirect('registerT')
	else:
		return render(request,'teachregform.html')
def accsp(request): #create account for service provider by admin
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
def requestFRSP(request): #teacher email entering to signup
	if 'email' in request.session:
		messages.info(request,'enter your correct email')
		current_email = constore.objects.get(email=request.session['email'])
		current_email.delete()
		request.session.flush()
		return redirect('requestFRSP')
	elif request.method == 'POST':
		email = request.POST['email']

		ck = Teacher.objects.filter(email=email)
		if ck.exists():
			request.session['email'] = email
			subject = 'confirmation code from ASTU ONLINE SUGGESTION BOX'
			rn = random.randint(100000,999999)
			message = 'confirmation number = ' + str(rn)
			from_email = settings.EMAIL_HOST_USER
			to_list = [email]

			send_mail(subject,message,from_email,to_list,fail_silently = True)
			store = constore(email=email,confirm=rn)
			store.save()
			return redirect('confirm')
		else:
			messages.info(request,'You are not elligable for service deal with the admin')
			return redirect('requestFRSP')
	else:
		return render(request,'emal.html')
def all(request): #displayed page whem initially the web is accessed
	return render(request,'all.html')
def login(request):#login for all user
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
			elif rl.role == 'student':
				auth.login(request,user)
				request.session['email']=user.email
				return redirect('studhome')
			else:
				return redirect('all')
		else:
			messages.info(request,'incorrect credential')
			return redirect('login')
	else:
		return render(request,'login.html')
def confirm(request): #check confirmation code thet sent to teacher and place for confirmation code
	if request.method == 'POST':
		confirmation_number_filled = request.POST['confirmation_code']

		confirmation_code = constore.objects.get(email=request.session['email'])
		print (confirmation_code.confirm)
		if (int(confirmation_number_filled) == int(confirmation_code.confirm) ):
			return redirect('signup_form')
		else:
			messages.info(request,'INCORRECT ENTRY CHECK THE NUMBER')
			return redirect('confirm')
	elif 'email' in request.session:
		return render(request,'confirmationcode.html',{'email':request.session['email']})
	else:
		messages.info(request,'first enter your email')
		return redirect('requestFRSP')
def logout(request):#logout for all user ecept the super admin
	auth.logout(request)
	messages.info(request,'you logged out successfully')
	return redirect('login')
def forteacher(request):# giving suggestion for teache
	instructors = Teacher.objects.all()
	return render(request,'forteacher.html',{'instructors':instructors})
def forsp(request):#giving suggestion for service provider
	service_providers = SP.objects.all()
	return render(request,'forsp.html',{'service_providers':service_providers})
def signup_form(request):#signup form for teacher
	if not 'email' in request.session:
		messages.info(request,'start from here')
		return redirect('requestFRSP') 
	elif request.method == 'POST':
		user_name = request.POST['user_name']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']

		if password == confirm_password:
			email = request.session['email']
			rol = "teacher"

			info_from_teacher = Teacher.objects.get(email=email)
			first_name = info_from_teacher.first_name
			last_name = info_from_teacher.last_name

			user = User.objects.create_user(first_name=first_name,last_name=last_name,username=user_name,email=email,password=password)
			user.save()

			role_set = role(username=user_name,role="teacher")
			role_set.save()

			current_email = constore.objects.get(email=request.session['email'])
			current_email.delete()
			request.session.flush()
			messages.info(request,'login to your account')
			return redirect('login')
	else:
		messages.info(request,'password does not match')
		return render(request,'teacher_signup_form.html')
def teacher_dash(request):# teacher dashboard
	if 'malda' in request.session:
		suggestions = Suggestions.objects.filter(suggestion_for='teacher',given_for=request.session['malda'])
		poster_id = request.session['malda']
		return render(request,'teachersdashboard.html',{'suggestions':suggestions,'poster_id':poster_id})
	else:
		messages.info(request,'login first')
		return redirect('login')	
def service_provider_dash(request):
	if 'malda' in request.session:
		suggestions = Suggestions.objects.filter(suggestion_for='service provider',given_for=request.session['malda'])
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
		private = request.POST['private']
		prvt = False
		if (private=='private'):
			prvt = True
		student_id = request.session['student_id']
		name = ''
		if (typ=='teacher'):
			namer = Teacher.objects.get(id=given_for)
			name = namer.first_name+' '+namer.last_name
		elif (typ == 'service provider'):
			namer = SP.objects.get(id=given_for)
			name = namer.service


		suggest = Suggestions(given_for = given_for,overall=overall,idea=suggestion,suggestion_for=typ,giver_id=student_id,name=name,private=prvt)
		suggest.save()
		messages.info(request,'succesfully given')
		if typ == 'service provider':
			return redirect('forsp')
		elif typ == 'teacher':
			return redirect('forteacher')
	else:
		return redirect('forsp')
def post(request):
	if request.method == 'POST':
		posted_from = request.POST['posted_from']
		poster_id = request.POST['poster_id']
		idea = request.POST['post']
		name = ''
		namer = User.objects.get(id=poster_id)
		name = namer.first_name+' '+namer.last_name
		post = POST(posted_from=posted_from,poster_id=poster_id,idea=idea,name=name)
		post.save()
		messages.info(request,'successfully posted')
		return redirect('post')
	else:
		post = POST.objects.filter(posted_from='teacher',poster_id=request.session['user_id'])
		return render(request,'post.html',{'posts':post})
def service_provider_post(request):
	if request.method == 'POST':
		posted_from = request.POST['posted_from']
		poster_id = request.POST['poster_id']
		idea = request.POST['post']

		post = POST(posted_from=posted_from,poster_id=poster_id,idea=idea)
		post.save()
		messages.info(request,'successfully posted')
		return redirect('service_provider_post')
	else:
		post = POST.objects.filter(posted_from='service provider',poster_id=request.session['user_id'])
		return render(request,'serviceprovider_post.html',{'posts':post})
def suggestions(request):
	givens = Suggestions.objects.filter(private='False')
	return render(request,'suggestions.html',{'givens':givens})
def posts(request):
	posts = POST.objects.all()
	return render(request,'posts.html',{'posts':posts})
def id(request):
	if request.method == 'POST':
		id = request.POST['id']
		request.session['id']=id
		return redirect('signup_student')
	else:
		return render(request,'id.html')
def signup_student(request):
	if 'id' in request.session:
		if request.method == 'POST':
			student_id = request.POST['student_id']
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			user_name = request.POST['user_name']
			email = request.POST['email']
			department = request.POST['department']
			year = request.POST['year']
			password1 = request.POST['password1']
			password2 = request.POST['password2']
			if (password1==password2):
				if(User.objects.filter(username=user_name).exists()):
					messages.info(request,'user name exists choose another user name')
					return redirect('signup_student')
				else:
					if (User.objects.filter(email=email).exists()):
						messages.info(request,'the same email exists choose anotherr email')
						return redirect('signup_student')
					else:
						user = User.objects.create_user(first_name=first_name,last_name=last_name,username=user_name,email=email,password=password1)
						Role = role(username=user_name,role='student')
						Student = student(department=department,email=email,year=year,student_id=student_id)

						user.save()
						Role.save()
						Student.save()
						
						request.session.flush()
						messages.info(request,'successfully created login to your account')
						return redirect('login')

			else:
				messages.info(request,'password doesnot match')
				return redirect('signup_student')
		else:
			id = request.session['id']
			return render (request,'signup_student.html',{'id':id})
	else:
		messages.info(request,'start here')
		return redirect('id')
def see_suggestions(request):
	if request.method == 'POST':
		user_name = request.POST['user_name']
		who = request.POST['who']
		user_id = ''
		if (who == 'teacher'):
			user_id = User.objects.get(username=user_name)
			user_id = Teacher.objects.get(email = user_id.email)
			user_id = user_id.id

			suggestions = Suggestions.objects.filter(given_for=user_id,suggestion_for='teacher')
			return render(request,'look_suggestions.html',{'Suggestions':suggestions})
		elif (who == 'service provider'):
			user_id = User.objects.get(username=user_name)
			user_id = SP.objects.get(email = user_id.email)
			user_id = user_id.id

			suggestions = Suggestions.objects.filter(given_for=user_id,suggestion_for='service provider')
			return render(request,'look_suggestions.html',{'Suggestions':suggestions})
	elif 'ID' in request.GET:
		ID = request.GET.get('ID')
		Student = student.objects.get(student_id = ID)
		Student_detail = User.objects.get(email = Student.email)
		return render(request,'look_suggestions.html',{'student':Student,'Student_detail':Student_detail})
	else:
		return render(request,'look_suggestions.html')