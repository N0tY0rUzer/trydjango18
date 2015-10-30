from django.db import models

# Create your models here.

class SignUp(models.Model):
	email = models.EmailField()

	# CharField w/max_length of 120 chars. Can be "blank"(option, default=False) in form; can be "null"(option; default=False) in DB
	full_name = models.CharField(max_length = 120, blank=True, null=True)

	# Timestamp when model is first created; none after that.
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	
	# Timestamp when model is updated; none before that.
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.email

