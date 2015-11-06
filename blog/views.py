
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context	
from  django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
def hello(request) :
	name = "Aryan"
	html = "<html> <body> Hi %s, This seems to have worked </body> </html>" %name
	return HttpResponse(html) 



def hello_template(request) :
	name = "Aryan"
	t  = get_template('hello.html')
	html = t.render(Context({'name' : name}))
	return HttpResponse(html) 

class HelloTemplate(TemplateView):
 	template_name = 'hello_class.html'

 	def get_context_data(self, **kwargs) :
 	 	context = super(HelloTemplate,self).get_context_data(**kwargs)
 	 	context['name'] = 'Aryan'
 	 	return context


def hello_template_simple(request):
	name  = 'Aryan'
	return render_to_response('hello.html' , {'name':name})