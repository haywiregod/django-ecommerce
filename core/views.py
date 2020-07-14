from django.shortcuts import render
from .models import Item,Order,OrderItem
from django.views.generic import ListView, DetailView
# Create your views here.

def index(request):
    context = {
        'items':Item.objects.all()
    }
    return render(request,'home-page.html',context)

def product(request):
    return render(request,'product-page.html')

def checkout(request):
    return render(request,'checkout-page.html')
class ItemListView(ListView):
    model = Item
    template_name = "home-page.html"

class ItemDetailView(DetailView):
    model = Item
    template_name = "product-page.html"
