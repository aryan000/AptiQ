from django.conf.urls import include,patterns,url
urlpatterns=patterns('',
url(r'^$','session.views.base',name='base'),

url(r'^main/$','session.views.main', name='main'),
url(r'^login/$','session.views.handleLogin', name='login'),
url(r'^signup/$','session.views.handleSignup', name='signup'),

url(r'^logout/$','session.views.logoutview', name='logout'),
)
