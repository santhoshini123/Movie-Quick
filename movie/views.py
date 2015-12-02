from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.conf import settings
from django.template import RequestContext, loader
import json
from .models import SignUp
<<<<<<< HEAD
import cgi
import os


=======
>>>>>>> ce9d6cf5dc1a52392c88f3d04c3dc7bf193ba42c
# Create your views here.

def index(request):
	return render(request, 'movie/register.html')

def register(request):
<<<<<<< HEAD
	return render(request,'movie/register.html')
=======
	return render(request,'register.html')
>>>>>>> ce9d6cf5dc1a52392c88f3d04c3dc7bf193ba42c


def validate(request):
	First_name=request.GET.get('firstname')
	Last_name=request.GET.get('lastname')
	Email=request.GET.get('usermail')
	password=request.GET.get('password')
	# Re_enter_password=request.GET.get('Re_enter_password')
	response = {}
	if not SignUp.objects.filter(Email=Email):
		m = SignUp(First_name=First_name,Last_name=Last_name,Email=Email,Password=password)
		m.save()
<<<<<<< HEAD
		# response['status']='success'
		return render(request,'index.html')
=======
		response['status']='success'
>>>>>>> ce9d6cf5dc1a52392c88f3d04c3dc7bf193ba42c
	else:
		response['status']='failure'
	json_data = json.dumps(response)
	return HttpResponse(json_data,content_type="application/json")

def validatelogin(request):
<<<<<<< HEAD
	email=request.POST.get('usermail')
	password=request.POST.get('Password')
	if  SignUp.objects.filter(Email=email,Password=password):
		# return HttpResponse("login success")
		return render(request,'index.html')
	else:
		return HttpResponse("Login Failed")
=======
    Email=request.POST.get('Email')
    password=request.POST.get('password')
    if movie.objects.filter(Email=Email,password=password):
        mov=movie.objects.filter(Email=Email,password=password)
        template = loader.get_template('movie/register.html')
        context = RequestContext(request, {
            'movie': movie,
        })
        return HttpResponse(template.render(context))
    else:
        return render_to_response('movie/register.html')


 
>>>>>>> ce9d6cf5dc1a52392c88f3d04c3dc7bf193ba42c
