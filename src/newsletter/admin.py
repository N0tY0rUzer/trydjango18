from django.contrib import admin

# Register your models here.

# Relative import .models
from .models import SignUp
# Relative import .forms
from .forms import SignUpForm

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__str__", "timestamp", "updated"]
	form = SignUpForm


admin.site.register(SignUp, SignUpAdmin)