from django.contrib import admin

# Register your models here.

# Relative import .models
from .models import SignUp
# Relative import .forms
from .forms import SignUpForm

'''Inherit the admin.ModelAdmin django object class'''
class SignUpAdmin(admin.ModelAdmin):

	'''Override list_display in admin with fields from model.'''
	list_display = ["__str__", "timestamp", "updated"]

	'''Use custom form in the admin edit portion of DB'''
	form = SignUpForm

'''Register admin site with SignUp model and custom admin page'''
admin.site.register(SignUp, SignUpAdmin)