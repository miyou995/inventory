from django import forms
from django.forms import ModelForm
from .models import Wilaya, Commune, WareHouseOrder, WareHouseOrderItem


class AddWilayaForm(ModelForm) :
    class Meta: 
        model = Wilaya 
        fields = '__all__' 
        
class AddCommuneForm(ModelForm) :
    class Meta: 
        model = Commune 
        fields = '__all__' 

class AddWareHouseOrderForm(ModelForm) :
    class Meta: 
        model = WareHouseOrder
        fields = '__all__' 

class AddWareHouseOrderItemForm(ModelForm) :
    class Meta: 
        model = WareHouseOrderItem
        fields = '__all__' 



