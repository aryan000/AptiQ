from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404,redirect,render
from .models import MyUser
from .forms import LoginForm,SignupForm
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
@require_GET
def base(request):
	if request.user.is_authenticated():
		return redirect('main')
	next_url=request.GET.get('next')
	signupform=SignupForm(initial={'phone':'+91'})
	loginform=LoginForm()
	data={'loginform':loginform,'signupform':signupform,'next':next_url}
	return render(request,'login.html',data)
@require_POST
def handleLogin(request):
	if request.user.is_authenticated():
		return redirect('main')
	f=LoginForm(request.POST)
	next_url=request.GET.get('next')
	if f.is_valid():
		user=f.get_user()
		login(request,user)
		if not next_url:
			return redirect('main')
		else :
			return redirect(next_url)
	else:
		loginform=f
		signupform=SignupForm(initial={'phone':'+91'})
		data={'signupform':signupform,'loginform':loginform,'next':next_url}
		return render(request,'account/base.html',data)
@require_POST
def handleSignup(request):
	if request.user.is_authenticated():
		return redirect('main')
	f=SignupForm(request.POST)
	next_url=request.GET.get('next')
	if f.is_valid():
		user=f.save()
		user.is_active=True
		user.save()
		return redirect('main')
	else:
		signupform=f
		loginform=LoginForm()
		data={'signupform':signupform,'loginform':loginform,'next':next_url}
		return render(request,'account/base.html',data)
@require_GET
@login_required
def main(request):
	questions = request.user.questions_asked.all();
	form=AnswerUploadForm();
	return render(request,'main.html',{'questions':questions,'form':form})
@require_GET
@login_required
def logoutview(request):
	if request.user.is_authenticated():
		logout(request)
		return redirect('base')

