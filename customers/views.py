from rest_framework import generics
from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerList(generics.ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
