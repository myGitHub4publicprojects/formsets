from django.test import TestCase
from django.urls import reverse

# Create your tests here.

from . import forms
from .models import Author, Book


class TestAuthorForm(TestCase):
    def test_empty_form(self):
        '''Should be invalid if no data is given'''
        form = forms.AuthorForm(data={})
        self.assertFalse(form.is_valid())


    def test_not_empty_form(self):
        '''Should be valid if data is given'''
        data = {'first_name': 'John', 'last_name': 'Smith'}
        form = forms.AuthorForm(data=data)
        self.assertTrue(form.is_valid())


class TestBookForm(TestCase):
    def test_empty_form(self):
        '''Should be invalid if no data is given'''
        form = forms.BookForm(data={})
        self.assertFalse(form.is_valid())

    def test_not_empty_form(self):
        '''Should be valid if data is given'''
        data = {'name': 'book1', 'pub_date': '1/1/1900'}
        form = forms.BookForm(data=data)
        self.assertTrue(form.is_valid())


class TestEditView(TestCase):
    def setUp(self):
        Author.objects.create(first_name='John', last_name='Smith')

    def test_if_works(self):
        '''when configured properly response.status code is 200'''
        url = reverse('edit', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_formset_post(self):
        '''should work if proper data in forms'''
        'NOTE: formset requires ManagementForm data to work not only forms'
        data = {
            # these are needed for formset to work
            'form-TOTAL_FORMS': 2,
            'form-INITIAL_FORMS': 0,
            
            # forms data
            'form-0-name': 'book1',
            'form-0-pub_date': '1/1/1900',
            'form-1-name': 'book2',
            'form-1-pub_date': '1/1/1900',
        }
        url = reverse('edit', args=(1,))
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)


    def test_formset_post_with_missing_date(self):
        '''should redirect if formset if not valid - no pub date in one form'''
        'NOTE: formset requires ManagementForm data to work not only forms'
        data = {
            # these are needed for formset to work
            'form-TOTAL_FORMS': 2,
            'form-INITIAL_FORMS': 0,
            
            # forms data
            'form-0-name': 'book1',
            'form-0-pub_date': '1/1/1900',
            'form-1-name': 'book2',
            'form-1-pub_date': '',
        }
        url = reverse('edit', args=(1,))
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

