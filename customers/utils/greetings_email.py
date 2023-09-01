from smtplib import SMTPServerDisconnected
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


class CustomerBirthdayGreetings:

    def __init__(self, customers):
        self.customers = customers
        self.company_name = settings.COMPANY_NAME
        self.from_email = settings.DEFAULT_FROM_EMAIL
        self.subject = f'🎉 Happy Birthday from {self.company_name}! 🎂'

    def send_greetings_email(self):

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
                print("Wrong email credentials!")