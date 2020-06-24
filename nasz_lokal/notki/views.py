from django.shortcuts import render, redirect
from .models import Category, Wpis
from .forms import AddCat, AddNote


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
    form=AddCat
    kwargs = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('notki_main')
        else:
            return redirect('notki_main')
    else:
        return render(request, 'notki/new_cat.html', kwargs)

def new_note(request, cat):
    form=AddNote()
    this_category= Category.objects.get(name=cat)
    kwargs={"form":form, "category":this_category}
    return render(request, 'notki/new_note.html', kwargs)


def add_note(request, cat):
    this_category = Category.objects.get(name=cat)
    categories= Category.objects.all()
    inst= Wpis(cat=this_category)
    form=AddNote(instance=inst,data=request.POST)
    kwargs = {"form": form, 'categories': categories}
    if form.is_valid():
        form.save()
        return redirect('notki_main')
    return redirect('notki_main')


def del_note(request,id):
    note_to_delete=Wpis.objects.get(pk=id)
    kwargs = {"wpis":note_to_delete}
    return render(request,'notki/del_page.html',kwargs)

def destroy_note(request,id):
    note_to_delete=Wpis.objects.get(pk=id)
    note_to_delete.delete()
    return redirect('notki_main')