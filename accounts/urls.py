from django.urls import path
from .views import SignupView, SignupsuccessView
from django.contrib.auth import views as auth_views
from .froms import AuthenticationForm
app_name= 'accounts'

urlpatterns = [
  
 path('signup/', SignupView.as_view(), name="signup"),
 path('signup_success/', SignupsuccessView.as_view(), name="signup_success"),
 path('login/', auth_views.LoginView.as_view(template_name="login.html",form_class=AuthenticationForm,),name="login",),
 path('logout/' , auth_views.LogoutView.as_view(), name= 'logout' ),
]




