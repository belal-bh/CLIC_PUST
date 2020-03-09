from django import forms

from .models import Book
from wishlist.models import (
    BookCart,
    ResourceCart
)

class BookForm(forms.ModelForm):
    class Meta:
        model = BookCart
        fields = []

class ResourceForm(forms.ModelForm):
    class Meta:
        model = ResourceCart
        fields = []