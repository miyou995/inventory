from itertools import product
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, UpdateView, DetailView
from pprint import pprint
from mptt.models import MPTTModel, TreeForeignKey
from .models import Product, Category, Brand, WareHouse, WareHouseItem
from .forms import AddProductForm, AddBrandForm, AddCategoryForm, AddWareHouseForm, AddWareHouseItemForm

# Create your views here.
## product
class ProductListView(ListView): 
    template_name= "product-list.html"
    model = Product 
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context["products"] =Product.objects.all().order_by('created')
        context["product_count"] =Product.objects.all().count()
        # filters=ProjectFilter(self.request.GET, queryset=Product.objects.all())
        # context["products"] = filters.qs
        return context
class ProductDetailView(DetailView):
    model = Product
    template_name= "product-detail.html"
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product_id = self.get_object().id
        context["products"] =Product.objects.all()
        context["warehouses"] = WareHouse.objects.all()
        context['warehouseitems'] = WareHouseItem.objects.all()
        context['instanceproduit'] = WareHouseItem.objects.filter(product=product_id)  
        return context 
class AddBrandView(CreateView):
    template_name= "add-brand.html"
    form_class= AddBrandForm
    model = Brand 
    success_url = reverse_lazy('inventory:productlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)

class AddCategoryView(CreateView):
    template_name= "add-category.html"
    form_class= AddCategoryForm
    model = Category 
    success_url = reverse_lazy('inventory:productlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(AddCategoryView, self).get_context_data(**kwargs)
        context["categorys"] = Category.objects.all()
        return context 

class AddProductView(CreateView):
    template_name= "add-product.html"
    form_class= AddProductForm
    model = Product 
    success_url = reverse_lazy('inventory:productlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(AddProductView, self).get_context_data(**kwargs)
        context["brands"] = Brand.objects.all()
        context["categorys"] = Category.objects.all()
        return context 

class ProductUpdateView(UpdateView):
    model = Product
    form_class= AddProductForm
    template_name = 'edit-product.html' 
    success_url = reverse_lazy('inventory:productlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context["brands"] = Brand.objects.all()
        context["categorys"] = Category.objects.all()
        return context 
##warehouse
class WarehouseListView(ListView): 
    template_name= "warehouse-list.html"
    model = WareHouse 
    def get_context_data(self, **kwargs):
        context = super(WarehouseListView, self).get_context_data(**kwargs)
        context["warehouses"] = WareHouse.objects.all().order_by('created')
        context["warehouse_count"] = WareHouse.objects.all().count()
        # filters=ProjectFilter(self.request.GET, queryset=Product.objects.all())
        # context["products"] = filters.qs
        return context

class AddWarehouseView(CreateView):
    template_name= "add-warehouse.html"
    form_class= AddWareHouseForm
    model = WareHouse 
    success_url = reverse_lazy('inventory:warehouselist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)

class WarehouseUpdateView(UpdateView):
    model = WareHouse
    form_class= AddWareHouseForm
    template_name = 'edit-warehouse.html' 
    success_url = reverse_lazy('inventory:warehouselist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)

class WarehouseDetailView(DetailView):
    model = WareHouse
    template_name= "warehouse-detail.html"
    def get_context_data(self, **kwargs):
        context = super(WarehouseDetailView, self).get_context_data(**kwargs)
        warehouse_id = self.get_object().id
        context["products"] =Product.objects.all().order_by('created')
        context['instanceproduit'] = WareHouseItem.objects.filter(location=warehouse_id)  
        return context 
## wraehouseitem
class AddWarehouseItemView(CreateView):
    template_name= "add-warehouseitem.html"
    form_class= AddWareHouseItemForm
    model = WareHouseItem 
    success_url = reverse_lazy('inventory:warehouselist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(AddWarehouseItemView, self).get_context_data(**kwargs)
        context["products"] =Product.objects.all().order_by('created')
        context["warehouses"] = WareHouse.objects.all()
        return context 