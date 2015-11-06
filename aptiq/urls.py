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
from session import urls as session_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/session/',include(session_urls)),
    url(r'^$','account.views.index',name='index'),
    url(r'^index/$','account.views.index',name='index'),
    url(r'^index/login/$','account.views.login',name='login'),
    url(r'^index/buy$','account.views.buy',name='buy'),
    url(r'^index/buy_single$','account.views.buy_single',name='buy_single'),
    url(r'^index/career$','account.views.career',name='career'),
    url(r'^index/contact$','account.views.contact',name='contact'),
    url(r'^index/dealer$','account.views.dealers',name='dealer'),
    url(r'^index/faq$','account.views.faqs',name='faq'),
    url(r'^index/feedback$','account.views.feedback',name='feedback'),
    url(r'^index/loan$','account.views.loan',name='loan'),
    url(r'^index/loan_single$','account.views.loan_single',name='loan_single'),
    url(r'^index/mobile_app$','account.views.mobile_app',name='mobile_app'),
    url(r'^index/privacy$','account.views.privacy',name='privacy'),
    url(r'^index/register$','account.views.register',name='register'),
    url(r'^index/single$','account.views.single',name='single'),
    url(r'^index/suggestion$','account.views.suggestion',name='suggestion'),
    url(r'^index/table$','account.views.table',name='table'),
    url(r'^index/terms$','account.views.terms',name='terms'),
    url(r'^index/typo$','account.views.typo',name='typo'),
    url(r'^index/blog$','account.views.blog',name='blog'),
    url(r'^home/$','account.views.home'),
    url(r'^index/blog_single$','account.views.blog_single',name='blog_single'),
    url(r'^about$','account.views.about',name='about'),


]       
