from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# Relative import .models
from .models import SignUp
# Relative import .forms
from .forms import SignUpForm

from accounts.models import SomeUser
from accounts.forms.register import RegistrationForm


'''Inherit the admin.ModelAdmin django object class'''
class SignUpAdmin(admin.ModelAdmin):

	'''Override list_display in admin with fields from model.'''
	list_display = ["__str__", "timestamp", "updated"]

	'''Use custom form in the admin edit portion of DB'''
	form = SignUpForm

'''Register admin site with SignUp model and custom admin page'''

class MyUserAdmin(UserAdmin):
	form = RegistrationForm

	list_display = ('email', 'is_admin')
	list_filter = ('is_admin',)
	fieldsets = (
		(None, {'fields': ('email',
		'password')}),
		('Permissions', {'fields': ('is_admin', 'is_superuser')})
	)

	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()

admin.site.register(SignUp, SignUpAdmin)
admin.site.register(SomeUser, MyUserAdmin)
