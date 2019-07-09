from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
 
    path('', views.catalog, name='catalog'),
    path('product/<int:prod_id>', views.product, name="product"),
    path('cart/', views.cart, name='cart'),
    path('cart/remove/', views.removefromcart, name='remove'),
    path('cart/checkout/', views.checkout, name='checkout'),
    path('cart/checkout/complete/', views.completeOrder, name='complete_order'),
    path('admin-login/', views.adminLogin, name='admin_login'),
    path('admin-panel/', views.adminDashboard, name='admin'),

]