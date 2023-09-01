from datetime import datetime
from smtplib import SMTPServerDisconnected
from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from customers.models import Customer


@shared_task
def send_birthday_greetings_email():

    customers = Customer.objects.filter(birthdate=datetime.today().date()).values("email", "name")
    for customer in customers:
        subject = f'🎉 Happy Birthday from {settings.COMPANY_NAME}! 🎂'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = customer["email"]

        # Load and render the HTML template
        html_content = render_to_string('birthday_email_template.html', {
            'name': customer["name"],
            'company_name': settings.COMPANY_NAME,
        })

        print(html_content)
        # Send email
        try:
            msg = EmailMultiAlternatives(subject, '', from_email, [to_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        except SMTPServerDisconnected as err:
            print("Wrong email credentials!")
