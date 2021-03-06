from django.forms import ModelForm
from .models import Author, Book


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class BookForm(ModelForm):
    class Meta:
        model = Book
        # fields = ['name', 'pub_date']
        exclude = ('author',)
