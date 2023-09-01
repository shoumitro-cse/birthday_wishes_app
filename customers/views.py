from rest_framework import generics
from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerListCreateAPIView(generics.ListCreateAPIView):
    """
    This API allows you to register new customers and retrieve a list of existing customers.

    Usage:
      - To register a new customer, send a POST request with the required data.
      - To retrieve a list of customers, send a GET request.

    Endpoint Details:
      - POST: Create a new customer.
      - GET: Retrieve a list of customers.

    Example Usage:

    - To register a customer:
      ```
          POST /api/customers/
          {
            "name": "John Doe",
            "email": "john@example.com",
            "birthday": "1990-05-15"
          }
      ```

    - To retrieve a list of customers:
      ```
         GET /api/customers/
      ```

    Response:
      - When registering a customer, you will receive a confirmation.
      - When retrieving a list of customers, you will get a list of customer records.
    """

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CustomerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    This API view allows you to Retrieve, Update, or Delete a specific customer.

    Usage:
      - To retrieve customer details, send a GET request specifying the customer's unique identifier.
      - To update customer information, send a PUT or PATCH request with the updated data.
      - To delete a customer record, send a DELETE request.

    Endpoint Details:
      - GET: Retrieve customer details by providing the customer's unique identifier.
      - PUT/PATCH: Update customer information by specifying the customer's unique identifier and the data to be updated.
      - DELETE: Delete a customer record by specifying the customer's unique identifier.

    Example Usage:

    - To retrieve customer details:
      ```
        GET /api/customers/{customer_id}/
      ```

    - To update customer information:
      ```
          PUT /api/customers/{customer_id}/
          {
            "name": "Updated Name",
            "email": "updated@example.com",
            "birthday": "1990-05-15"
          }
      ```

    - To delete a customer:
      ```
        DELETE /api/customers/{customer_id}/
      ```

    Response:
      - When retrieving customer details, you will receive the customer's information.
      - When updating customer information, you will receive a confirmation.
      - When deleting a customer, you will receive a confirmation.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

