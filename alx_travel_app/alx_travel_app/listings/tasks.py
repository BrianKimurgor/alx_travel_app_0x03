from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(recipient_email, booking_id):
    subject = 'Booking Confirmation'
    message = f'Thank you for your booking! Your booking ID is {booking_id}.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [recipient_email]
    send_mail(subject, message, email_from, recipient_list)