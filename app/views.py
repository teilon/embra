from django.shortcuts import render, redirect, get_object_or_404
from .transaction import product_item_fill

from .forms import NewClientForm, NewTransactionForm
from .models import \
    PartnerSet, \
    TransactionSet, \
    StorageSet, \
    ProductItem


def index(request):
    context = {}
    return render(request, 'app/index.html', context)


def temp(request):
    context = {}
    return render(request, 'app/temp.html', context)


def index1(request):
    context = {}
    return render(request, 'app/index1.html', context)


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
    # init_storage()
    product_item_fill()
    # test_receipt()

    context = {}
    return render(request, 'app/storage.html', context)


def client_list(request):
    clients = PartnerSet.objects.all()
    context = {'clients': clients}
    return render(request, 'app/client_list.html', context)


def client_detail(request, pk):
    client = PartnerSet.objects.get(pk=pk)
    context = {'client': client}
    return render(request, 'app/client_detail.html', context)


def client_new(request):
    if request.method == 'POST':
        form = NewClientForm(request.POST)
        if form.is_valid():
            new_client = form.save(commit=False)
            print(request.user)
            context = {'form': form}
            return render(request, 'app/client_new.html', context)

    form = NewClientForm()
    context = {'form': form}
    return render(request, 'app/client_new.html', context)


def create_storage(request, name):
    items = []
    products = ProductItem.objects.all()
    for p in products:
        items.append(p.code)

    context = {
        'name': name,
        'items': items
    }


def client_edit(request, pk):
    client = get_object_or_404(PartnerSet, pk=pk)
    if request.method == 'POST':
        form = NewClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            print(request.user)
            # client.author = request.user
            # client.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = NewClientForm(instance=client)
    context = {'form': form, 'pk': pk}
    return render(request, 'app/client_edit.html', context)


def transaction_list(request):
    transactions = TransactionSet.objects.all()
    context = {'transactions': transactions}
    return render(request, 'app/transaction_list.html', context)


def transaction_new(request):
    form = NewTransactionForm()
    context = {'form': form}
    return render(request, 'app/transaction_new.html', context)


def show_storage(request):
    ps = StorageSet.objects.first().product_set_id
    context = {}
    return render(request, 'app/storage.html', context)

