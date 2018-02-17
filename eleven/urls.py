from django.conf.urls import url
from eleven.views import HomeView, AboutView

app_name = 'home'

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^about/$', AboutView.as_view(), name='about'),
]