from django import forms

class LoginForm(forms.Form):
	login = forms.EmailField(label='Login')
	password = forms.CharField(label='Password', max_length=80)

class RegisterFrom(forms.Form):
	name = models.CharField('User name', max_length=80)
	email = models.EmailField('Email')
	password = models.CharField('Password', max_length=80)