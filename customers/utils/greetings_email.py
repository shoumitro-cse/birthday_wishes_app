from smtplib import SMTPServerDisconnected
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


class CustomerBirthdayGreetings:
    """
    This class is responsible for sending birthday greetings emails to a list of customers.

    Attributes:
    - customers: A list of customer dictionaries, each containing 'name' and 'email' fields.
    - company_name: The name of the company sending the greetings (configured in Django settings).
    - from_email: The default sender email address (configured in Django settings).
    - subject: The subject line of the birthday greetings email.

    Methods:
    - send_greetings_email: Sends birthday greetings emails to the customers in the list.
    """

    def __init__(self, customers):
        """
        Initialize the CustomerBirthdayGreetings instance.

        Args:
        - customers: A list of customer dictionaries, each containing 'name' and 'email' fields.
        """
        self.customers = customers
        self.company_name = settings.COMPANY_NAME
        self.from_email = settings.DEFAULT_FROM_EMAIL
        self.subject = f'🎉 Happy Birthday from {self.company_name}! 🎂'

    def send_greetings_email(self):
        """
        Sends birthday greetings emails to the specified customers.
        """

        for customer in self.customers:
            # Load and render the HTML template
            html_content = render_to_string(template_name='birthday_email_template.html', context={
                'name': customer["name"],
                'company_name': self.company_name,
            })
            # Send email
            try:
                msg = EmailMultiAlternatives(self.subject, from_email=self.from_email, to=[customer["email"]])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            except SMTPServerDisconnected as err:
                print("Failed to send birthday greetings email: Wrong email credentials!")
