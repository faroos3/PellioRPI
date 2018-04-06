from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect

from .forms import GAD7Form

def index(request):
	print("Home page")
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			user = authenticate(username=request.POST['username'],password = request.POST['password'])
			if user is not None:
				auth_login(request, user)
				return redirect('/dash')
			else:
				return render(request, 'home/dash-nouser.html')
	else:
		form = AuthenticationForm()
	if request.user.is_authenticated:
		return HttpResponseRedirect('/dash')
	return render(request, 'home/home.html', {'form': form})


# Basic idea: if user not authenticated, redirected them to home. If they are, fulfill request.
def signupdash(request):
	return render(request, 'home/dash.html')
	
def gad7(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect('../')
	return render(request, 'home/GAD7.html')
	
def phq9(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect('../')
	return render(request, 'home/PHQ9.html')
	
def dash(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect('../')
	return render(request, 'home/dash.html')
	
def gad7sub(request):
	if request.method == 'POST':
		form = GAD7Form(request.POST)
		if form.is_valid():
			feild1 = form.cleaned_data['feild1']
			feild2 = form.cleaned_data['feild2']
			feild3 = form.cleaned_data['feild3']
			feild4 = form.cleaned_data['feild4']
			feild5 = form.cleaned_data['feild5']
			feild6 = form.cleaned_data['feild6']
			feild7 = form.cleaned_data['feild7']
			p = Person(feild1=feild1, feild2=feild2, feild3=feild3, feild4=feild4, feild5=feild5, feild6=feild6, feild7=feild7)
			p.save()
			return render(request, 'home/wtf')
	else:
		form = GAD7Form()
	return render(request, 'home/wtf')
	
		
			
	
def phq9sub(request):
	return HttpResponseRedirect('home/wtf')
	if not request.user.is_authenticated:
		return HttpResponseRedirect('home/home.html')
	return HttpResponseRedirect('/dash')