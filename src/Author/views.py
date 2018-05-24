from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm

from django.forms.formsets import formset_factory

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
    BookFormSet = formset_factory(BookForm, extra=2)

    if request.method == "POST":
        formset = BookFormSet(request.POST)
        if(formset.is_valid()):
            print('formset ok')
            # do domething with forms
            for form in formset:
                instance = form.save(commit=False)
                instance.author = author
                instance.save()
        else:
            # if formset is not valid do something else
            print('FAULT in formset')
            # to see which form was faulty:
            for form in formset:
                if not form.is_valid():
                    print('this form was not valid: ', form.errors)
            return redirect('home')
    context = {'author': author,
               'books': author.book_set.all(),
               'formset': BookFormSet()
               }
    return render(request, 'edit.html', context)

