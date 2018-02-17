from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from authentication.forms import LoginForm

app_name='auth'

urlpatterns = [
    url(r'^$', login, {'template_name': 'authentication/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]
