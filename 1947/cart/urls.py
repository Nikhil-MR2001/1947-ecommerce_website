from django.urls import path, include
from . import views

app_name = 'cart'



urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:id>', views.remove_from_cart, name='remove_from_cart'),

]