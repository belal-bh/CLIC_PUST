from django import forms

from resource.models import (
    Book,
    Resource,
    Author,
)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = []

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = []


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = []
