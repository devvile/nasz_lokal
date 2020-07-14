from django.shortcuts import render, redirect
from .models import Category, Wpis
from .forms import AddCat, AddNote
from django.contrib.auth.decorators import login_required


@login_required
def main(request):
    categories = Category.objects.all()
    kwargs={'categories':categories}
    return render(request, 'notki/main.html', kwargs)

@login_required
def detail(request, id):
    categoria= Category.objects.get(pk=id)
    notki= categoria.nalezace.all()
    kwargs={"cat":categoria,"notki":notki}
    return render(request, 'notki/detail.html', kwargs)

@login_required
def del_cat(request, cat):
    categoria= Category.objects.get(name=cat)
    kwargs={"cat":categoria}
    return render(request, 'notki/del_cat.html', kwargs)

@login_required
def destroy_cat(request, id):
    categoria= Category.objects.get(pk=id)
    categoria.delete()
    return redirect('notki_main')

@login_required
def new_cat(request):
    form=AddCat()
    kwargs = {"form": form}
    return render(request, 'notki/new_cat.html', kwargs)


@login_required
def new_note(request, cat):
    form=AddNote()
    this_category= Category.objects.get(name=cat)
    kwargs={"form":form, "category":this_category}
    return render(request, 'notki/new_note.html', kwargs)

@login_required
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

@login_required
def add_cat(request):
    form=AddCat(data=request.POST)
    kwargs = {"form": form}
    if form.is_valid():
        form.save()
        return redirect('notki_main')
    return redirect('notki_main')

@login_required
def del_note(request,id):
    note_to_delete=Wpis.objects.get(pk=id)
    kwargs = {"wpis":note_to_delete}
    return render(request,'notki/del_page.html',kwargs)

@login_required
def destroy_note(request,id):
    note_to_delete=Wpis.objects.get(pk=id)
    note_to_delete.delete()
    return redirect('notki_main')

def edit_page(request,id):
    that_note= Wpis.objects.get(pk=id)
    data = {"name":that_note.name ,"note":that_note.note}
    form = AddNote(data)
    this_cat = Category.objects.get(nalezace=that_note)
    kwargs={"form":form, "wpis":that_note, "cat":this_cat, "note":that_note}
    return render(request,'notki/edit_page.html', kwargs)

def update_note(request, id):
    note = Wpis.objects.get(pk=id)
    x = request.POST
    note.name = x["name"]
    note.note=  x["note"]
    note.save()
    return redirect('notki_main')