from django import forms
from .models import SignUp

'''This is a Form class from django for non model forms'''
class ContactForm(forms.Form):
	'''We set the fields right in the form since there is no model'''
	full_name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()


'''This is a ModelForm, a django class for implementing forms that work with the DB'''
class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name','email']

	'''Override default builtin django validation with "def clean_<field>(self)" method.
	This can be used with any field in a form. '''
	def clean_email(self):

		'''Grab the email if passed initial validation. This is what django is doing, if it passes this, inspect further before submitting'''
		email = self.cleaned_data.get('email')
		'''Split the email into a base name and a provider e.g jcain, gmail.com'''
		email_base, provider = email.split("@")
		'''Split the provider into domain and extension e.g gmail.com'''
		domain, extension = provider.split('.')
		'''If the extension is not edu, raise django forms builtin ValidationError'''
		if not extension == 'edu':
			raise forms.ValidationError("Please use a valid .edu email address.")
		return email
