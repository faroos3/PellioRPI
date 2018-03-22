from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    if request.user.is_authenticated:
        return HttpResponseRedirect('../')
    return render(request, 'accounts/signup.html', {'form': form})