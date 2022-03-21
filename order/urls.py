from django.urls import path
from . import views 
from .views import AddWilayaView, AddCommuneView, AddWareHouseOrderView
from django.contrib.auth.decorators import login_required, permission_required
app_name= 'order'

urlpatterns = [
  

   
   #commune wilaya 
  
   path('addwilaya', login_required(AddWilayaView.as_view()), name="addwilaya"),
   path('addcommune', login_required(AddCommuneView.as_view()), name="addcommune"),
   path('addwilaya', login_required(AddWareHouseOrderView.as_view()), name="addwarehouseorder"),
  
 

]




