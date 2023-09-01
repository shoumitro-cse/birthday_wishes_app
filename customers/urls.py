from django.urls import path
from customers.views import CustomerListCreateAPIView, CustomerRUDAPIView

urlpatterns = [
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerRUDAPIView.as_view(), name='customer-detail'),
]
