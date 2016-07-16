from .forms import Userform2
from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate ,login,logout
from .models import *
from django.views import generic
from django.http.response import HttpResponse
import json, random ,re, requests,urllib,urllib.request
from pprint import pprint
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist

def home(request):
	q='Vancouver, BC, Canada'
	w='San Francisco, CA, USA'
	url="https://maps.googleapis.com/maps/api/distancematrix/json?origins="+q+"&destinations="+w+"&key=AIzaSyB7qtuTdcnDb6Dl4BrmsZyxIMrUMpwhHW0"
	ds = requests.get(url).json()
	a=ds['destination_addresses']
	b=ds['rows'][0]['elements'][0]['distance']['text']
	return HttpResponse(b)

def add_warehouse(request):
	if request.user.is_authenticated() and Userform.objects.get(user=request.user).flag==1:
		if request.method=="GET":
			return render(request,'add_warehouse.html',{})
		else:
			obj=warehouse.objects.create(user=request.user.username,location=request.POST.get('location'),cold_total=request.POST.get('cold'),cold_available=request.POST.get('cold'),severe_total=request.POST.get('severe'),severe_available=request.POST.get('severe'),mild_total=request.POST.get('mild'),mild_available=request.POST.get('mild'),hot_total=request.POST.get('hot'),hot_available=request.POST.get('hot'))
			obj.save()
			return HttpResponseRedirect('/')
	elif Userform.objects.get(user=request.user).flag==2:
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/account/login')




def register(request):
	if request.method=='POST':
		form=Userform2(request.POST)
		if form.is_valid():
			user=form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user2=authenticate(username=username,password=password)
			if user2 is not None:
				login(request,user2)
				return HttpResponseRedirect('/index/')
		return render(request,'registration.html',{'form':form})
	else:
		form=Userform2(None)
		return render(request,'registration.html',{'form':form})

def logintoit(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return HttpResponseRedirect('/index/')
		return render(request,'login.html',{})

	else:
		return render(request,'login.html',{})

def logout1(request):
	logout(request)
	return HttpResponseRedirect('/account/login/')
	
def index(request):
	if request.user.is_authenticated():
		user=request.user
		if request.method=="GET":
			try :
				obj=Userform.objects.get(user=user)
				return HttpResponseRedirect('/')
			except ObjectDoesNotExist:
				return render(request,'index.html',{})
		else:
			temp=request.POST.get('flag')
			if temp=='ware':
				sam=Userform.objects.create(user=user,flag=1)
				sam.save()
			else:
				sam=Userform.objects.create(user=user,flag=2)
				sam.save()
			return HttpResponseRedirect('/')


