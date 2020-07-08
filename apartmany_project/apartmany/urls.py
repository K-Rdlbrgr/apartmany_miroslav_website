from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('studios/', views.studios, name='studios'),
    path('apartments/', views.apartments, name='apartments'),
    path('surroundings/', views.surroundings, name='surroundings'),
    path('guestbook/', views.guestbook, name='guestbook'),
    path('gallery/', views.gallery, name='gallery'),
    path('prices_and_faqs/', views.prices_and_faqs, name='prices_and_faqs'),
    path('contact/', views.contact, name='contact'),
]