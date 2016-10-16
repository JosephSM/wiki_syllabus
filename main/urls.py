"""Define URL patterns for the main app."""

from . import views
from django.conf.urls import url

app_name = 'main'
urlpatterns = [
	#Home page
	url(r'^$', views.home_page, name="home"),
	#Create account link
	url(r'^create_account/$', views.regact, name="create_account"),

	#Register account link
	url(r'^create_account/reg/', views.create_account, name="register_account"),
	url(r'^rrr', views.register_account, name='rrr'),
	url(r'^home', views.home_page, name='home')

	#url(r'^users/', include('users.urls', namespace = 'users')),

]