from django.shortcuts import render
from django.http import HttpResponse
from .models import Test
# Create your views here.
def home(request):
	return render(request,"home.html",{})

# def test(request):
# 	test = Test.objects.all()
# 	return render(request,"test.html",{'Data':test})	