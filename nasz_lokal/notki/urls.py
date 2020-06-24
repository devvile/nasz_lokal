from django.urls import path
from .views import main, detail

urlpatterns = [
    path('main', main, name='notki_main'),
    path('detail/<int:id>', detail, name='detail'),
]
