from django.shortcuts import render

# Create your views here.
from itertools import product
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, UpdateView, DetailView
from pprint import pprint
from mptt.models import MPTTModel, TreeForeignKey
from .models import Wilaya, Commune, WareHouseOrder, WareHouseOrderItem
from .forms import AddWilayaForm, AddCommuneForm, AddWareHouseOrderForm, AddWareHouseOrderItemForm
from accounts.models import User 
# Create your views here.
## wilaya commune

class AddWilayaView(CreateView):
    template_name= "add-wilaya.html"
    form_class= AddWilayaForm
    model = Wilaya 
    success_url = reverse_lazy('order:addwilaya')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
class AddCommuneView(CreateView):
    template_name= "add-commune.html"
    form_class= AddCommuneForm
    model = Commune 
    success_url = reverse_lazy('order:addcommune')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(AddCommuneView, self).get_context_data(**kwargs)
        context["wilayas"] = Wilaya.objects.all()
        return context 
##commande depot 
class AddWareHouseOrderView(CreateView):
    template_name= "add-product.html"
    form_class= AddWareHouseOrderForm
    model = WareHouseOrder 
    success_url = reverse_lazy('order:addwarehouseorder')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(AddWareHouseOrderView, self).get_context_data(**kwargs)
        context["wilayas"] = Wilaya.objects.all()
        context["senders"] = User.objects.all()
        context["receivers"] = User.objects.all()
        return context 
