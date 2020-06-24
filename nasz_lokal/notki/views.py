from django.shortcuts import render
from .models import Category, Wpis

def main(request):
    categories = Category.objects.all()
    kwargs={'categories':categories}
    return render(request, 'notki/main.html', kwargs)

def detail(request, id):
    notki= Wpis.objects.all()
    '''
    musimy sciagnac categorie po id i od niej wejsc w foreign key wszystkie co ja maja
    '''
    kwargs={}
    return render(request, 'notki/detail.html', kwargs)