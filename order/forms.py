from django import forms
from django.forms import ModelForm
from .models import WareHouseOrder, WareHouseOrderItem
from django.forms.models import inlineformset_factory, modelformset_factory
from location.models import Wilaya, Commune 

class WilayaForm(ModelForm) :
    class Meta: 
        model = Wilaya 
        fields = '__all__' 
        
class CommuneForm(ModelForm) :
    class Meta: 
        model = Commune 
        fields = '__all__' 

class WareHouseOrderForm(ModelForm) :
    class Meta: 
        model = WareHouseOrder
        fields = ('receiver', 'delivery_man', 'order_type', 'is_confirmed', 'is_paid', 'is_delivered', 'is_return', 'discount', 'delivery_cost', 'note')

class WareHouseOrderItemForm(ModelForm) :
    custom = forms.IntegerField(required=False)
    class Meta: 
        model = WareHouseOrderItem
        fields = ("order","warehouse_item","quantity","price",)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        # self.fields['custom'] = forms.IntegerField()

class ProductInternalOrder(forms.Form):
    product = forms.CharField( required=True)
    quantity = forms.IntegerField()
    # reference = 