from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm

# Create your views here.
def home(request):
    # displays a list of authors
    
    return render(request, 'home.html', {'authors': Author.objects.all()})

def create(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'create.html', {'form': form})


def edit(request, pk):
    author = Author.objects.get(pk=pk)
    form = BookForm(request.POST or None)
    context = {'author': author,
               'books': author.book_set.all(),
               'form': form}
    return render(request, 'edit.html', context)

