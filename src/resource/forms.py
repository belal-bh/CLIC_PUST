from django import forms

from .models import Book
from wishlist.models import (
    BookCart,
    ResourceCart
)

class BookCartForm(forms.ModelForm):
    class Meta:
        model = BookCart
        fields = []

class ResourceCartForm(forms.ModelForm):
    class Meta:
        model = ResourceCart
        fields = []