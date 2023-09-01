from django.urls import path
from customers.views import CustomerList, CustomerDetailView

urlpatterns = [
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
]
