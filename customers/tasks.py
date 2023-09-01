from datetime import datetime
from celery import shared_task
from customers.models import Customer
from customers.utils.greetings_email import CustomerBirthdayGreetings


@shared_task
def send_birthday_greetings_email():
    """
    Task:
      - Sends birthday greetings emails to customers whose birthday matches the current date.
      - Retrieves the list of eligible customers from the database and uses the
      - CustomerBirthdayGreetings class to send the greetings.
    """

    # Get a list of customers whose birthday is today and select 'email' and 'name' fields
    customers_today = Customer.objects.filter(birthdate=datetime.today().date()).values("email", "name")

    # Create an instance of CustomerBirthdayGreetings and send greetings emails
    birthday_greetings_sender = CustomerBirthdayGreetings(customers_today)
    birthday_greetings_sender.send_greetings_email()
