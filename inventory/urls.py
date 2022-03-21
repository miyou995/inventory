from django.urls import path
from . import views 
from .views import AddProductView, AddBrandView, AddCategoryView, ProductListView, ProductUpdateView,AddWarehouseView, WarehouseListView, WarehouseUpdateView, AddWarehouseItemView, WarehouseDetailView, ProductDetailView
from django.contrib.auth.decorators import login_required, permission_required
app_name= 'inventory'

urlpatterns = [
  
   #PRODUCT
   path('productlist', login_required(ProductListView.as_view()), name='productlist'),
   path('editproduct/<int:pk>/', login_required(ProductUpdateView.as_view()), name="editproduct"),
   path('productdetail/<int:pk>/', login_required(ProductDetailView.as_view()), name="productdetail"),
   path('addbrand', login_required(AddBrandView.as_view()), name="addbrand"),
   path('addcategory', login_required(AddCategoryView.as_view()), name="addcategory"),
   path('addproduct', login_required(AddProductView.as_view()), name="addproduct"),
   
   #WAREHOUSE 
   path('warehouselist', login_required(WarehouseListView.as_view()), name='warehouselist'),
   path('addwarehouse', login_required(AddWarehouseView.as_view()), name="addwarehouse"),
   path('editwarehouse/<int:pk>/', login_required(WarehouseUpdateView.as_view()), name="editwarehouse"),
   path('warehousedetail/<int:pk>/', login_required(WarehouseDetailView.as_view()), name="warehousedetail"),
   ##Warehouseitem
   path('addwarehouseitem', login_required(AddWarehouseItemView.as_view()), name="addwarehouseitem"),
 

]




