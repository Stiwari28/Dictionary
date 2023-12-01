from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
#username: STiwari
#password: 1731
def home(request):
    return render(request, 'index.html')