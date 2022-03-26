from django.shortcuts import render

# Create your views here.
from itertools import product
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, UpdateView, DetailView
from pprint import pprint
from mptt.models import MPTTModel, TreeForeignKey
from .models import WareHouseOrder, WareHouseOrderItem
from location.models import Wilaya, Commune 
from inventory.models import WareHouseItem , WareHouse
from .forms import WilayaForm, CommuneForm, WareHouseOrderForm, WareHouseOrderItemForm, ProductInternalOrder
from accounts.models import User 
from django.conf import settings
from django.forms import formset_factory, modelformset_factory, inlineformset_factory
from django.contrib import messages


# User = settings.AUTH_USER_MODEL

# Create your views here.
## wilaya commune
##### a deplacer dans location views
class WilayaView(CreateView):
    template_name= "add-wilaya.html"
    form_class= WilayaForm
    model = Wilaya 
    success_url = reverse_lazy('order:addwilaya')

    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
class CommuneView(CreateView):
    template_name= "add-commune.html"
    form_class= CommuneForm
    model = Commune 
    success_url = reverse_lazy('order:addcommune')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(CommuneView, self).get_context_data(**kwargs)
        context["wilayas"] = Wilaya.objects.all()
        return context 
##commande depot 

class WareHouseOrderView(CreateView):
    template_name= "add-product.html"
    form_class= WareHouseOrderForm
    model = WareHouseOrder 
    success_url = reverse_lazy('order:addwarehouseorder')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(WareHouseOrderView, self).get_context_data(**kwargs)
        context["wilayas"] = Wilaya.objects.all()
        context["senders"] = User.objects.all()
        context["receivers"] = User.objects.all()
        return context 

# InternalOrderItemFormSet = inlineformset_factory (
#     WareHouseOrder,
#     WareHouseOrderItem,
#     form = WareHouseOrderItemForm,
#     min_num=0,  # minimum number of forms that must be filled in
#     extra=0,  # number of empty forms to display
# )

def add_new_item(request, param=None):
    the_number = param
    print('the num ', param)
    return render(request, "snippets/item_row_form.html", {'the_number':the_number})


def create_internal_order(request):
    princpale = WareHouse.centrale.principale()
    items = WareHouseItem.objects.filter(location=princpale)
    receivers = User.custom_objects.user_warehouses()
    order_form = WareHouseOrderForm(request.POST or None)
    product_formset = inlineformset_factory (
        WareHouseOrder,
        WareHouseOrderItem,
        fields=("warehouse_item","quantity"),
        form = WareHouseOrderItemForm,
        min_num=1, 
        extra=0,
    )
    formset = product_formset(request.POST or None)
    if request.method == "POST":
        print('user form')
        order_form = WareHouseOrderForm(request.POST)
        if order_form.is_valid():
            new_order = order_form.save(commit=False)
            new_order.order_type = "BC"
            new_order.save()
            for item_form in formset:
                print('one')
                if item_form.is_valid():
                    item = item_form.save(commit=False)
                    item.order = new_order
                    item.save()
                else: 
                    messages.error(request, form.errors)
            return reverse_lazy('order:warehouse_order_list')
            
        else: 
            messages.error(request, order_form.errors)
                    ###### add error message if not valid
    else :
        order_form = WareHouseOrderForm()
    context = {
        "formset": product_formset,
        "the_number" : 0,
        "receivers" :  receivers,
        "products" :  items,
        "order_form" : order_form
    }
    return render(request, "internal_order.html", context)


class WarehouseOrderListView(ListView): 
    model = WareHouseOrder
    template_name = "warehouse_order_list.html"
    context_object_name = "orders"
