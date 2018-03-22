from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect


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
	if not request.user.is_authenticated:
		return HttpResponseRedirect('home/home.html')
	return HttpResponseRedirect('/dash')
	
def phq9sub(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect('home/home.html')
	return HttpResponseRedirect('/dash')