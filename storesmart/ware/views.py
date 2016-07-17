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

def home2(request):
	all_ware=warehouse.objects.filter(user=request.user)
	return render(request,'home2.html',{'all':all_ware})

def orders(request):
	if request.user.is_authenticated():
		if request.method=='POST':
			order2=order.objects.create(user="sam",ware_owner="viru",quantity=100,price=1000,type_of="mild")
			order2.save()

			#order1=order.objects.create(user=request.user.username,ware_owner=request.POST.get('owner'),quantity=request.POST.get('quantity'),type_of=request.POST.get('type_of'),price=1000)
			#order1.save()
			return render(request,'order_completed.html',{'order2':order2})

def home(request):
	if request.user.is_authenticated() and Userform.objects.get(user=request.user).flag==1:
		return home2(request)
	c={}
	b=""
	stat=0
	if 'txtSource' in request.POST:
		arr=warehouse.objects.all()
		for a in arr:
			w=a.location
			q=request.POST['txtSource']
			url="https://maps.googleapis.com/maps/api/distancematrix/json?origins="+q+"&destinations="+w+"&mode=driving&language=en-EN&key=AIzaSyB7qtuTdcnDb6Dl4BrmsZyxIMrUMpwhHW0"
			ds = requests.get(url).json()
			if  ds['status']!="OK" or ds['rows'][0]['elements'][0] ['status']!="OK":
				continue
			a=ds['destination_addresses']
			c[w]=ds['rows'][0]['elements'][0]['distance']['text']
		

		stat=1
		for k in sorted(c, key=c.get, reverse=True):
  			print (k)
  			b=k
  			break

  	
	if not b:
		b="Not Available Any"
		owner=""
	else:
		owner=warehouse.objects.get(location=b).user
	context = {
	'stat':stat,
	'b':b,
	'type_of':request.POST.get('inlineRadioOptions'),
	'quantity':request.POST.get('totalmaterial'),
	'owner':owner,


	} 

	return render(request,'abc.html',context)
	
def edit_warehouse(request,id):
	if request.user.is_authenticated() and Userform.objects.get(user=request.user).flag==1:
		if request.method=="GET":
			ware=warehouse.objects.get(id=id)
			print (ware)
			return render(request,'edit_warehouse.html',{'ware':ware})
		else:
			ware=warehouse.objects.get(id=id)
			ware.user=request.user.username
			ware.location=request.POST.get('location')
			ware.cold_available=request.POST.get('cold')
			ware.severe_available=request.POST.get('severe')
			ware.mild_available=request.POST.get('mild')
			ware.hot_available=request.POST.get('hot')
			ware.cold_rate=request.POST.get('cold_rate')
			ware.mild_rate=request.POST.get('mild_rate')
			ware.hot_rate=request.POST.get('hot_rate')
			ware.severe_rate=request.POST.get('severe_rate')
			ware.save()
			return HttpResponseRedirect('/')
	elif Userform.objects.get(user=request.user).flag==2:
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/account/login')
		
def add_warehouse(request):
	if request.user.is_authenticated() and Userform.objects.get(user=request.user).flag==1:
		if request.method=="GET":
			return render(request,'add_warehouse.html',{})
		else:
			obj=warehouse.objects.create(user=request.user.username,location=request.POST.get('location'),cold_total=request.POST.get('cold'),cold_available=request.POST.get('cold'),severe_total=request.POST.get('severe'),severe_available=request.POST.get('severe'),mild_total=request.POST.get('mild'),mild_available=request.POST.get('mild'),hot_total=request.POST.get('hot'),hot_available=request.POST.get('hot'),cold_rate=request.POST.get('cold_rate'),hot_rate=request.POST.get('hot_rate'),mild_rate=request.POST.get('mild_rate'),severe_rate=request.POST.get('severe_rate'))
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

