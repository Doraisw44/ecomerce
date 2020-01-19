from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView
from core.models import *

# Create your views here.
def base_view(request):
    return render(request,'core/base.html')
class ListViews(ListView):
    model=item
    template_name='core/home-page.html'
    fields='__all__'
class DetailViews(DetailView):
    model=item
    template_name='core/product-page.html'


def add_to_cart(request,item):
    it=item.objects.get(item=item)
    or_it=orderitem.objects.create(order_item=it)
    or_it.save()

