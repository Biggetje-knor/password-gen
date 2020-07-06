from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
# def home(request):
#     return HttpResponse("<h1>Hello there friend!</h1>")
# def eggs(request):
#     return HttpResponse("<h1>Eieren zijn heel lekker!</h1>")

def home(request):
    return render(request,"generator/home.html")

def about(request):
    return render(request,'generator/about.html')


def password(request):

    characters = list("abcdefbhijklmnopqrstuvwxyz")
    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVW"))

    if request.GET.get("numbers"):
        characters.extend(list("0123456789"))

    if request.GET.get("special"):
        characters.extend(list("~!@#$%^&*()_+=-`"))

    length = int(request.GET.get('length',12))

    thepassword = ''

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/password.html',{'password':thepassword})

