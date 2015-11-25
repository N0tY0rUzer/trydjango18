from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import SomeUser

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    password = ReadOnlyPasswordHashField

    class Meta:
        model = SomeUser
        fields = ('email', 'password', 'is_active', 'is_admin', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
