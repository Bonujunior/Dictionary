from django.shortcuts import render
from django.http import HttpResponse
from .models import Dictionary


# Create your views here.
def index(request):
    word = request.GET.get('q', '')
    if word and word != '':
        search = Dictionary.objects.filter(eng__contains = word).all()[:4]
    
        
    else:
        search = None
        
    context = {'q': word , 'search': search}
    return render(request, 'home.html', context)




