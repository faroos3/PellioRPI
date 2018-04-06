from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .forms import GAD7Form
from .forms import PHQ9Form
from .forms import HomeForm

def index(request):
	print("Home page")
	Hfirst = ''
	Hsecond = ''
	Hthird = ''
	Hfourth = ''
	Hfifth = ''
	Hsixth = ''
	Hseventh = ''
	Heighth = ''
	Hninth = ''
	Htenth = ''
	Heleventh = ''
	if request.method == 'GET':
		homeform = HomeForm(request.POST or None)
		if homeform.is_valid():
			return render(request, 'home/success.html')
			Hfirst = homeform.cleaned_data['first']
			Hsecond = homeform.cleaned_data['second']
			Hthird = homeform.cleaned_data['third']
			Hfourth = homeform.cleaned_data['fourth']
			Hfifth = homeform.cleaned_data['fifth']
			Hsixth = homeform.cleaned_data['sixth']
			Hseventh = homeform.cleaned_data['seventh']
			Heigth = homeform.cleaned_data['eighth']
			Hninth = homeform.cleaned_data['ninth']
			Htenth = homeform.cleaned_data['tenth']
			Heleventh = homeform.cleaned_data['eleventh']
			return render(request, 'home/success.html')
			
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
	Gfirst = ''
	Gsecond = ''
	Gthird = ''
	Gfourth = ''
	Gfifth = ''
	Gsixth = ''
	Gseventh = ''
	if not request.user.is_authenticated:
		return HttpResponseRedirect('../')
	if request.method == 'POST':#They tried to submit something
		gad7form = GAD7Form(request.POST or None)
		if gad7form.is_valid():
			Gfirst = gad7form.cleaned_data['first']
			Gsecond = gad7form.cleaned_data['second']
			Gthird = gad7form.cleaned_data['third']
			Gfourth = gad7form.cleaned_data['fourth']
			Gfifth = gad7form.cleaned_data['fifth']
			Gsixth = gad7form.cleaned_data['sixth']
			Gseventh = gad7form.cleaned_data['seventh']
			return render(request, 'home/success.html')
		else:
			return render(request, 'home/invalid.html')
		return render(request, 'home/dash.html')
	return render(request, 'home/GAD7.html')
	
def phq9(request):
	Pfirst = ''
	Psecond = ''
	Pthird = ''
	Pfourth = ''
	Pfifth = ''
	Psixth = ''
	Pseventh = ''
	Peighth = ''
	Pninth = ''
	
	if not request.user.is_authenticated:
		return HttpResponseRedirect('../')
	if request.method == 'POST':#They tried to submit something
		form = PHQ9Form(request.POST or None)
		if form.is_valid():
			Pfirst = form.cleaned_data['first']
			Psecond = form.cleaned_data['second']
			Pthird = form.cleaned_data['third']
			Pfourth = form.cleaned_data['fourth']
			Pfifth = form.cleaned_data['fifth']
			Psixth = form.cleaned_data['sixth']
			Pseventh = form.cleaned_data['seventh']
			Peighth = form.cleaned_data['eighth']
			Pninth = form.cleaned_data['ninth']
			return render(request, 'home/success.html')
		else:
			return render(request, 'home/invalid.html')
		return render(request, 'home/dash.html')
	return render(request, 'home/PHQ9.html')
	
def dash(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect('../')
	return render(request, 'home/dash.html')
