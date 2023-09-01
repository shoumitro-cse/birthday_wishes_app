from datetime import datetime
from celery import shared_task
from customers.models import Customer
from customers.utils.greetings_email import CustomerBirthdayGreetings


@shared_task
def send_birthday_greetings_email():
    customers = Customer.objects.filter(birthdate=datetime.today().date()).values("email", "name")
    birthday_gr = CustomerBirthdayGreetings(customers)
    birthday_gr.send_greetings_email()
