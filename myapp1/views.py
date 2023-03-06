from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Type, Item
import calendar

# Create your views here.

def index(request):
    type_list = Type.objects.all().order_by('id')[:7]
    return render(request, 'myapp1/index0.html', {'type_list': type_list})


def about(request):
    return render(request, 'myapp1/about0.html')

def detail(request, type_no):
    typeReq = get_object_or_404(Type, pk=type_no)
    items = Item.objects.filter(type=typeReq)
    return render(request, 'myapp1/detail0.html', {'type': typeReq, 'item_list': items})

def items(request):
    itemlist = Item.objects.all().order_by('id')[:20]
    return render(request, 'myapp1/items.html', {'itemlist': itemlist})

def placeorder(request):
    return render(request, 'myapp1/placeorder.html')



