from django import forms

from .models import Professor

class Create_account_form(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField( max_length=100)
	email = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100)

		
