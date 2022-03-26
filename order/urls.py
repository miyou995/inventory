from django.urls import path
from . import views 
from .views import WilayaView, CommuneView, WareHouseOrderView, create_internal_order, add_new_item, WarehouseOrderListView
from django.contrib.auth.decorators import login_required, permission_required
app_name= 'order'

urlpatterns = [
  

   
   #commune wilaya 
  
   path('addwilaya', login_required(WilayaView.as_view()), name="addwilaya"),
   path('add_new_item', add_new_item, name="add_new_item"),
   path('addcommune', login_required(CommuneView.as_view()), name="addcommune"),
   path('addwilaya', login_required(WareHouseOrderView.as_view()), name="addwarehouseorder"),
   path('warehouse_order_list', login_required(WarehouseOrderListView.as_view()), name="warehouse_order_list"),
   path('create_internal_order', login_required(create_internal_order), name="create_internal_order"),
  
 

]




