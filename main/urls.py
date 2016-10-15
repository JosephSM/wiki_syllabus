"""Define URL patterns for the main app."""

from . import views
from django.conf.urls import url

urlpatterns = [
	#Home page
	url(r'^$', views.home_page, name="home"),
	#Create account link
	url(r'^create_account.html$', views.create_account, name="create_account")

]