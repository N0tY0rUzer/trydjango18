from django import forms

class AuthenticationForm(forms.Form):
    ''' Login Form '''

    email = forms.EmailField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ['email', 'password']
