from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.conf import settings
from django.template import RequestContext, loader
import json
from .models import SignUp
import cgi
import os


# Create your views here.

def index(request):
	return render(request, 'movie/register.html')

def register(request):
	return render(request,'movie/register.html')


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
		# response['status']='success'
		return render(request,'index.html')
	else:
		response['status']='failure'
	json_data = json.dumps(response)
	return HttpResponse(json_data,content_type="application/json")

def validatelogin(request):
	email=request.POST.get('usermail')
	password=request.POST.get('Password')
	if  SignUp.objects.filter(Email=email,Password=password):
		# return HttpResponse("login success")
		return render(request,'index.html')
	else:
		return HttpResponse("Login Failed")