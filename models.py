from django.db import models

# Create your models here.
class admin(models.Model):
class role(models.Model):
class Teacher(models.Model):
class SP(models.Model):
class constore(models.Model):
class Suggestions(models.Model):
	suggestion_for = models.CharField(max_length=100)
	given_for = models.CharField(max_length=100)
	overall = models.CharField(max_length=20)
	idea = models.TextField()
	given_time = models.DateTimeField(auto_now=True, auto_now_add=False)
	privacy = models.boolean()
class POST(models.Model):