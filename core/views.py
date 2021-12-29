import string
import random

from django.shortcuts import render
from core.models import Password


def index(request):
    password_list = Password.objects.all()
    return render(request, 'core/index.html', context={'password_list': password_list})


def gen_password():
    password = ''
    for _ in range(10):
        letter = random.choice(string.ascii_lowercase)
        password += letter
    for _ in range(3):
        letter = random.choice(string.ascii_uppercase)
        password += letter

    for _ in range(2):
        digit = random.choice(string.digits)
        password += digit
    list_password = list(password)
    new_password = ''
    for i in range(15):
        index = random.choice(range(len(list_password)))
        letter = list_password.pop(index)
        new_password += letter

    return new_password


def generate_password(request):
    password = gen_password()
    Password.objects.create(password=password)
    password_list = Password.objects.all()
    return render(request, 'core/password_created.html', context={
        'password': password,
        'password_list': password_list
    })


def keto_index(request):
    return render(request, 'core/index1.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def blog(request):
    return render(request, 'core/blog.html')


def gallery(request):
    return render(request, 'core/gallery.html')


def room(request):
    return render(request, 'core/room.html')