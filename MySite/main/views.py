from django.shortcuts import render, redirect
from .models import Items
from .forms import ItemsForm
from django.views.generic import UpdateView, DeleteView


def index(request):
    return render(request, 'main/index.html')


def stock(request):
    items = Items.objects.all()
    return render(request, 'main/stock.html', {'items': items})


def create(request):
    error =''
    if request.method == 'POST':
        form = ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock')
        else:
            error = 'Запись неверная'

    form = ItemsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)


class update(UpdateView):
    model = Items
    template_name = 'main/create.html'

    form_class = ItemsForm


class delete(DeleteView):
    model = Items
    success_url = '/delete/'
    template_name = 'main/delete.html'


def login(request):
    return render('main/base.html')







