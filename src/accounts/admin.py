from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from accounts.models import SomeUser
from accounts.forms.register import RegistrationForm
from accounts.forms.user_change import UserChangeForm


class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = RegistrationForm
    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email',
        'password', 'joined')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_superuser')})
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'joined', 'is_active', 'is_admin', 'is_superuser')
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(SomeUser, MyUserAdmin)
admin.site.unregister(Group)
