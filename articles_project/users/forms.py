from django import forms

class LoginForm(forms.Form):
	login = forms.EmailField(label='Login')
	password = forms.CharField(label='Password', max_length=80)

class RegisterFrom(forms.Form):
	name = forms.CharField(label='User name', max_length=80)
	email = forms.EmailField(label='Email')
	password = forms.CharField(label='Password', max_length=80)