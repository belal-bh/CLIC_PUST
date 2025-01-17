# account.admin.py

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('library_id', 'email', 'admin')
    list_filter = ('admin', 'active', 'account_type')

    fieldsets = (
        (None, {'fields': ('library_id', 'email', 'password')}),
        ('Personal info', {'fields': (
            'name',
            'father_name',
            'mother_name',
            'gender',
            'mailing_address',
            'permanent_address',
            'contact_mobile',
            'contact_phone',
            'image',
        )}),
        ('Official info', {'fields': (
            'account_type',
            'registration_copy',
            'validity',
            'active',
        )}),
        ('Permissions', {'fields': ('admin', 'staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('library_id', 'email', 'password1', 'password2')}
         ),
    )
    search_fields = ('library_id', 'email')
    ordering = ('library_id', 'email')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
