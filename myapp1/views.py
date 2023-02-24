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
    type = get_object_or_404(Type, id=type_no)
    items=type.objects.filter(type=type)
    return render(request, 'myapp1/detail0.html', {'type': type, 'item_list':items })



