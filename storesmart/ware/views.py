from .forms import Userform
from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate ,login,logout

def register(request):
	if request.method=='POST':
		form=Userform(request.POST)
		if form.is_valid():
			user=form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user2=authenticate(username=username,password=password)
			if user2 is not None:
				login(request,user2)
				return HttpResponseRedirect('/')
		return render(request,'registration.html',{'form':form})
	else:
		form=Userform(None)
		return render(request,'registration.html',{'form':form})

def logintoit(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return HttpResponseRedirect('/')
		return render(request,'login.html',{})

	else:
		return render(request,'login.html',{})

def logout1(request):
	logout(request)
	return HttpResponseRedirect('/account/login/')


