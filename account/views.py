from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
	return render(request,"index.html")
	
def home(request):
		return render(request,"index.html")

def login(request):
	return render(request,"login.html")

def buy(request):
	return render(request,"buy.html")
	
def buy_single(request):
	return render(request,"buy_single.html")
def buy(request):
	return render(request,"buy.html")
	
def career(request):
	return render(request,"career.html")

def contact(request):
	return render(request,"contact.html")

def dealer(request):
	return render(request,"dealers.html")

def dealers(request):
	return render(request,"dealers.html")

def faqs(request):
	return render(request,"faqs.html")

def faq(request):
	return render(request,"faqs.html")

def feedback(request):
	return render(request,"feedback.html")

def loan(request):
	return render(request,"loan.html")

def loan_single(request):
	return render(request,"loan_single.html")

def mobile_app(request):
	return render(request,"mobile_app.html")

def privacy(request):
	return render(request,"privacy.html")
	
def register(request):
	return render(request,"register.html")

def single(request):
	return render(request,"single.html")

def suggestion(request):
	return render(request,"suggestion.html")
	
def table(request):
	return render(request,"table.html")

def about(request):
	return render(request,"about.html")
	
def terms(request):
	return render(request,"terms.html")
def blog(request):
	return render(request,"blog.html")

def blog_single(request):
	return render(request,"blog_single.html")
def typo(request):
	return render(request,"typo.html")
	