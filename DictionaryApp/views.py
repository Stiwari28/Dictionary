from django.shortcuts import render, get_object_or_404
from .models import Word
from .forms import WordSearchForm

from django.http import HttpResponse

# Create your views here.

# def home(request):
 #   return render(request, 'home.html')


def search_word(request):
    if request.method == 'POST':
        form = WordSearchForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            word_details = get_object_or_404(Word, word__iexact=word)
            
            return render(request, 'search_word.html', {'word_details': word_details})
    else:
        form = WordSearchForm()

    return render(request, 'search_word.html', {'form': form})
