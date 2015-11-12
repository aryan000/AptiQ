"""aptiq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','mainaccount.views.index',name='index'),
    url(r'^index/$','mainaccount.views.index',name='index'),
    url(r'^index/login/$','mainaccount.views.login',name='login'),
    url(r'^index/buy$','mainaccount.views.buy',name='buy'),
    url(r'^index/buy_single$','mainaccount.views.buy_single',name='buy_single'),
    url(r'^index/career$','mainaccount.views.career',name='career'),
    url(r'^index/contact$','mainaccount.views.contact',name='contact'),
    url(r'^index/dealer$','mainaccount.views.dealers',name='dealer'),
    url(r'^index/faq$','mainaccount.views.faqs',name='faq'),
    url(r'^index/feedback$','mainaccount.views.feedback',name='feedback'),
    url(r'^index/loan$','mainaccount.views.loan',name='loan'),
    url(r'^index/loan_single$','mainaccount.views.loan_single',name='loan_single'),
    url(r'^index/mobile_app$','mainaccount.views.mobile_app',name='mobile_app'),
    url(r'^index/privacy$','mainaccount.views.privacy',name='privacy'),
    url(r'^index/register$','mainaccount.views.register',name='register'),
    url(r'^index/single$','mainaccount.views.single',name='single'),
    url(r'^index/suggestion$','mainaccount.views.suggestion',name='suggestion'),
    url(r'^index/table$','mainaccount.views.table',name='table'),
    url(r'^index/terms$','mainaccount.views.terms',name='terms'),
    url(r'^index/typo$','mainaccount.views.typo',name='typo'),
    url(r'^index/blog$','mainaccount.views.blog',name='blog'),
    url(r'^home/$','mainaccount.views.home'),
    url(r'^index/blog_single$','mainaccount.views.blog_single',name='blog_single'),
    url(r'^about$','mainaccount.views.about',name='about'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^test$','mainaccount.views.test',name='test'),
    url(r'^index/contact$','mainaccount.views.contact',name='contact'),
    url(r'^contact$','mainaccount.views.contact1',name='contact1'),



]       
