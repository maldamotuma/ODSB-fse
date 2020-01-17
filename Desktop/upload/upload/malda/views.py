from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class home(TemplateView):
	templateName = 'home.html'
def upload(request):
	return render(request,'upload.html')
