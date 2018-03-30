from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

def dash(request):	
	return render(request, 'dash/dash-nouser.html')
	
