from django.db import models

# Create your models here.
class role(models.Model):
	username = models.CharField(max_length=100)
	role = models.CharField(max_length=100)
class Teacher(models.Model):
class SP(models.Model):
class constore(models.Model):
	email = models.CharField(max_length=200)
	confirm = models.IntegerField()
class Suggestions(models.Model):
class POST(models.Model):
	
