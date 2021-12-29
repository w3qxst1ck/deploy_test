from django.urls import path

from core.views import *

urlpatterns = [
    path('', index),
    path('generate-password/', generate_password, name='generate-password'),
    path('home/', keto_index, name='index-page'),
    path('about/', about, name='about-page'),
    path('blog/', blog, name='blog-page'),
    path('room/', room, name='room-page'),
    path('contact/', contact, name='contact-page'),
    path('gallery/', gallery, name='gallery-page'),
]
