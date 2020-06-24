from django.shortcuts import render, redirect
from .models import Category, Wpis
from .forms import AddCat

def main(request):
    categories = Category.objects.all()
    kwargs={'categories':categories}
    return render(request, 'notki/main.html', kwargs)

def detail(request, id):
    categoria= Category.objects.get(pk=id)
    notki= categoria.nalezace.all()
    kwargs={"cat":categoria,"notki":notki}
    return render(request, 'notki/detail.html', kwargs)

def delete_cat(request, id):
    categoria= Category.objects.get(pk=id)
    notki= categoria.nalezace.all()
    kwargs={"cat":categoria,"notki":notki}
    return render(request, 'notki/detail.html', kwargs)

def new_cat(request):
    form=AddCat()
    kwargs = {"form": form}
    return render(request, 'notki/new_cat.html', kwargs)

def add_cat(request):
    form=AddCat()
    kwargs = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('notki_main')
        else:
            return redirect('notki_main')
    else:
        return render(request, 'notki/new_cat.html', kwargs)

