from django.contrib import admin
from django.urls import path, include
from telcomedy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('telcomedy/', include('telcomedy.urls')),
    path('',include('telcomedy.urls')),
    
]
