
from django import forms

class WordSearchForm(forms.Form):
    word = forms.CharField(label='Enter a word', max_length=100)
