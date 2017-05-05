from django.shortcuts import render
from django.shortcuts import render_to_response
from mainaccount.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.http import HttpResponseRedirect , HttpResponse 

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'core/home.html')
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

def contact1(request):
	form_class= ContactForm
	#new logic
	if request.method == 'POST':
		form = form_class(data=request.POST)
		if form.is_valid():
			contact_name = request.POST.get('contact_name','')
			contact_email= request.POST.get('contact_email','')			
			form_content = request.POST.get('content','')
			#Email the profile with the contact information
			template = get_template('contact_template.txt')
			context = Context({'contact_name': contact_name,'contact_email': contact_email,
				'form_content': form_content,})
			content = template.render(context)
			email = EmailMessage("New contact form submission",content,"Your website" +'<hi@weddinglovely.com>',
				['youremail@gmail.com'],headers = {'Reply-To': contact_email })
			email.send()
			return redirect('contact')

	return render(request,'contact1.html',{'form' : form_class,})

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
def sampletest(request):
	return render(request,"test.html")

def starttest(request):
	return render(request,"starttest.html") 

def leveltest(request):
	return render(request,"leveltest.html")
def leveltest2(request):
	return render(request,"leveltest2.html")
def graph4beg(request):
	return render(request,"g4b.html")

def p2b(request):
	return render(request,"p2b.html")

def p3b(request):
	return render(request,"p3b.html")


 