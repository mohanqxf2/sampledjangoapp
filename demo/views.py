from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def index(request):
	return render(request, "demo/index.html", {})


def loginuser(request):
	if request.method == 'GET':
		return render(request, "demo/loginuser.html", {'form': AuthenticationForm()})
	else:
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is None:
			return render(request, "demo/loginuser.html", {'form': AuthenticationForm(), 'error': 'Incorrect Username or Password'})
		else:
			login(request, user)
			return redirect('index')


@login_required
def logoutuser(request):
	if request.method == 'POST':
		logout(request)
		return redirect('index')					