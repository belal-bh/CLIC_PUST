# account.forms.py
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# from pagedown.widgets import PagedownWidget

from django.contrib.auth import get_user_model
from django.db.models import Q
# datetimepicker
# from bootstrap_datepicker_plus import DateTimePickerInput, DatePickerInput

User = get_user_model()
# from .models import User


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'father_name',
            'mother_name',
            'gender',
            'mailing_address',
            'permanent_address',
            'contact_mobile',
            'contact_phone',
            'image',
            'account_type',
            'registration_copy',
            'library_id',
            'validity',
            'active',
            'staff',
            'admin'
        )

    def clean_library_id(self):
        library_id = self.cleaned_data.get('library_id')
        qs = User.objects.filter(library_id=library_id)
        if qs.exists():
            raise forms.ValidationError("library_id is taken")
        return library_id

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'father_name',
            'mother_name',
            'gender',
            'mailing_address',
            'permanent_address',
            'contact_mobile',
            'contact_phone',
            'image',
            'account_type',
            'registration_copy',
            'library_id',
            'validity',
            'active',
            'staff',
            'admin'
        )

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super(UserUpdateForm, self).save(commit=False)
        # user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class LoginForm(forms.Form):
    query = forms.CharField(label='Library_id / Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        query = self.cleaned_data.get('query')
        password = self.cleaned_data.get('password')
        user_qs_final = User.objects.filter(
            Q(library_id__iexact=query) |
            Q(email__iexact=query)
        ).distinct()

        if not user_qs_final.exists() and user_qs_final.count != 1:
            raise forms.ValidationError(
                "Invalid credentials - user does note exist")
        user_obj = user_qs_final.first()
        if not user_obj.check_password(password):
            raise forms.ValidationError("credentials are not correct")
        if not user_obj.is_active:
            raise forms.ValidationError("This user is not longer active.")
        self.cleaned_data["user_obj"] = user_obj

        return super(LoginForm, self).clean(*args, **kwargs)
