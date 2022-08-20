
from django.shortcuts import render

from .models import Contact, Subscribe


def main(request):

    return render(request, 'main.html')


def subscribe(request):
    if request.method == "POST":
        subscribe = Subscribe()
        email = request.POST.get('email')
        name = request.POST.get('name')
        subscribe.email = email
        subscribe.name = name
        subscribe.save()

    return render(request, 'subscribe.html')


def mperfume(request):

    return render(request, 'mperfume.html')


def mtester(request):

    return render(request, 'mtester.html')


def fperfume(request):

    return render(request, 'fperfume.html')


def ftester(request):

    return render(request, 'ftester.html')


def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()

    return render(request, 'contact.html')


def pay(request):

    return render(request, 'pay.html')


def paypal(request):

    return render(request, 'paypal.html')
