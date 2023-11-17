from django.forms import ModelForm
from .models import Book,Author

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title','description', 'author', 'year']

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name'] 