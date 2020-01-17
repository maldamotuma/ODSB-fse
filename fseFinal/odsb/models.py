from django.db import models

# Create your models here.
class admin(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	user_name = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	password = models.TextField()
class role(models.Model):
	username = models.CharField(max_length=100)
	role = models.CharField(max_length=100)
class Teacher(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	department = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
class SP(models.Model):
	service = models.TextField()
	email = models.CharField(max_length=200)
class constore(models.Model):
	email = models.CharField(max_length=200)
	confirm = models.IntegerField()
class Suggestions(models.Model):
	suggestion_for = models.CharField(max_length=100)
	given_for = models.CharField(max_length=100)
	overall = models.CharField(max_length=20)
	idea = models.TextField()
	given_time = models.DateTimeField(auto_now=True, auto_now_add=False)
class POST(models.Model):
	posted_from = models.CharField(max_length=100)
	poster_id = models.CharField(max_length=100)
	idea = models.TextField()
	given_time = models.DateTimeField(auto_now=True, auto_now_add=False)