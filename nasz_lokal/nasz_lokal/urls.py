
from django.contrib import admin
from django.urls import path, include
from .views import red

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cat/', include('notki.urls')),
    path('',red)
]
