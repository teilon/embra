from django.shortcuts import render


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


from .models import Storage, ProductSet, Client


def start_storage(request):
    context = {}
    has_client = Client.objects.count()
    if has_client == 0:
        create_provider()

    has_store = Storage.objects.count()
    if has_store != 0:
        return render(request, 'app/storage.html', context)
    product_set = create_product_set()
    create_storage(product_set)

    return render(request, 'app/storage.html', context)


def create_provider():
    provider = Client(name='ИП \"Баймуратов\"', form='PD')
    provider.save()


def create_product_set():
    product_set = ProductSet(m1=0, m2=0, m3=0, m4=0, m5=0, m6=0, m7=0, m8=0, m9=0, m10=0,
                             w1=0, w2=0, w3=0, w4=0, w5=0, w6=0, w7=0, w8=0, w9=0, w10=0)
    product_set.save()
    return product_set


def create_storage(product_set):
    storage = Storage(product_set=product_set)
    storage.save()

