from django.shortcuts import render

from .forms import ContactForm, SignUpForm

# Create your views here.
def home(request):
	title = "Welcome"

	'''Create SignUpForm object from POST data(if sent) or None if not sent'''
	form = SignUpForm(request.POST or None)
	'''Create context dict object; this will change if form.is_valid() returns true'''
	context = {
		"title": title,
		"form": form
	}


	'''Check to see if form has been validated and sent back'''
	if form.is_valid():
		#form.save()
		# print(request.POST['email']) # not recommended to grab variables from the post dictionary

		'''Save an instance of the validated form. Option commit=False allows us to save this ModelForm
		to memory, but not commit it to the DB just yet(i.e the instance). This allows us the option of further post processing
		and to populate things such as null=False fields, and to further secure that only clean data is passed to the DB'''
		instance = form.save(commit=False)

		'''It is advised to grab data from forms with the cleaned_data.get('<field>') method. 
		In this way, you can prevent from accidentally grabbing unsanitized data '''
		full_name = form.cleaned_data.get('full_name')
		

		'''Create a check for the full_name field from cleaned_data'''
		if not full_name:
			# If no full_name was set; create default name variable
			full_name = "New full name"

		'''Set the form instance\'s full_name field to the full_name variable'''
		instance.full_name = full_name
		
		'''Commit the form instance to the DB'''
		instance.save()

		'''Reset the context variable for render object to thank user for submission'''
		context = {
			"title": "Thank yee!"
		}
		
	return render(request, "home.html", context)


''''''
def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get('email')
		message = form.cleaned_data.get('message')
		full_name = form.cleaned_data.get("full_name")


	context = {
		"form": form
	}
	return render(request, "forms.html", context)