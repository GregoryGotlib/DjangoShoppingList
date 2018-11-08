from django.contrib import admin
from django.urls import path,include
from shoppinglist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shoppinglist.urls')),
]
