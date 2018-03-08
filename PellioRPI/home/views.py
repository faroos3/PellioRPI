from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

def index(request):
	print("Home page")
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			user = authenticate(username=request.POST['username'],password = request.POST['password'])
			if user is not None:
				auth_login(request, user)
				return render(request, 'home/dash.html')
			else:
				return render(request, 'home/dash-nouser.html')
	else:
		form = AuthenticationForm()
	return render(request, 'home/home.html', {'form': form})
