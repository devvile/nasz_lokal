from django.urls import path
from .views import main, detail,new_cat, add_cat,new_note,add_note,del_note,destroy_note, del_cat, destroy_cat

urlpatterns = [
    path('main', main, name='notki_main'),
    path('detail/<int:id>', detail, name='detail'),
    path('new_cat',new_cat, name='new_category'),
    path('add_cat',add_cat,name='add_cat'),
    path('del_cat/<str:cat>', del_cat, name='del_cat'),
    path('destroy_cat/<int:id>', destroy_cat, name='destroy_cat'),
    path('<str:cat>/new_note',new_note,name='new_note'),
    path('<str:cat>/add_note', add_note, name='add_note'),
    path('<int:id>/del_note', del_note, name='del_note'),
    path('<int:id>/destroy_note', destroy_note, name='destroy_note')
]
