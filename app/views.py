from django.shortcuts import render
from .transaction import init_storage


def index(request):
    context = {}
    return render(request, 'app/index.html', context)


def index2(request):
    context = {}
    return render(request, 'app/index2.html', context)


def index3(request):
    context = {}
    return render(request, 'app/index3.html', context)


def storage(request):
    context = {}
    return render(request, 'app/storage.html', context)


def start_storage(request):    
    init_storage()

    context = {}
    return render(request, 'app/storage.html', context)

