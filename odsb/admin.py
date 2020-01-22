from django.contrib import admin
from .models import role
from django.shortcuts import render, redirect

# Register your models here.
admin.site.site_header = 'ASTU DIGITAL SUGGESTION BOX SUPER USER'
def register_admin(request):
    if request.method == 'POST':
        return redirect('/')
    else:
        return render(request,'forteacher.html')
admin.site.register(role)
