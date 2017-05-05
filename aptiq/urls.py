"""aptiq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from mainaccount import views 

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'

urlpatterns = [
   url(r'^admin/', include(admin.site.urls)),

    url(r'^$',views.index,name='index'),
    #  this is used for social login
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--

    url(r'^index/$',views.index,name='index'),
    url(r'^index/login/$',views.login,name='login'),
    url(r'^index/$',views.index,name='index'),
    url(r'^index/login/$',views.login,name='login'),
    url(r'^index/buy$',views.buy,name='buy'),
    url(r'^index/buy_single$',views.buy_single,name='buy_single'),
    url(r'^index/career$',views.career,name='career'),
    url(r'^index/contact$',views.contact,name='contact'),
    url(r'^index/dealer$',views.dealers,name='dealers'),
    url(r'^index/faq$',views.faqs,name='faqs'),
    url(r'^index/feedback$',views.feedback,name='feedback'),
    url(r'^index/loan$',views.loan,name='loan'),
    url(r'^index/loan_single$',views.loan_single,name='loan_single'),
    url(r'^index/mobile_app$',views.mobile_app,name='mobile_app'),
    url(r'^index/privacy$',views.privacy,name='privacy'),
    url(r'^index/register$',views.register,name='register'),
    url(r'^index/single$',views.single,name='single'),
    url(r'^index/suggestion$',views.suggestion,name='suggestion'),
    url(r'^index/table$',views.table,name='table'),
    url(r'^index/terms$',views.terms,name='terms'),
    url(r'^index/typo$',views.typo,name='typo'),
    url(r'^index/blog$',views.blog,name='blog'),
    
    url(r'^index/blog_single$',views.blog_single,name='blog_single'),
    url(r'^about$',views.about,name='about'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^sample/test$',views.sampletest,name='sampletest'),
    url(r'^index/contact$',views.contact,name='contact'),
    url(r'^contact$',views.contact1,name='contact1'),
    url(r'^starttest$',views.starttest,name='starttest'),
    url(r'^leveltest$',views.leveltest,name='leveltest'),
    url(r'^graph4beg$',views.graph4beg,name='graph4beg'),
    url(r'^level2$',views.leveltest2,name='leveltest2'),
    url(r'^p2b$',views.p2b,name='p2b'),
    url(r'^p3b$',views.p3b,name='p3b'),
    
    

]
