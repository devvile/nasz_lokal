from django.urls import path
from .views import main, detail,new_cat, add_cat

urlpatterns = [
    path('main', main, name='notki_main'),
    path('detail/<int:id>', detail, name='detail'),
    path('new_cat',new_cat, name='new_category'),
    path('add_cat',add_cat,name='add_cat')
]
