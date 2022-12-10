from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.index), #index
   path('about/',views.about), #about
   path('contact/',views.contact), #contact
]