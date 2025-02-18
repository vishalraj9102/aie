import random
from django.core.mail import send_mail

def generate_otp():
    return str(random.randint(100000, 999999))

def send_email(to_email, message):
    send_mail('Your OTP', message, 'vishalrajmehra95@gmail.com', [to_email], fail_silently=False)