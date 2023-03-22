from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_otp import devices_for_user
from django.core.mail import send_mail, EmailMessage
from django_otp.plugins.otp_email.models import EmailDevice
from django_otp.forms import OTPTokenForm
from django.contrib.auth.signals import user_logged_in

user = get_user_model()

# @receiver(post_save, sender=user)
# def create_email_otp_device(sender, instance, created, **kwargs):
#     print("Called function")
#     print(instance)
#     print(sender)
#     email=instance.email
#     devices = list(devices_for_user(instance))
#     if devices:
#         print("Assigned email")
#         print(f"devices: {devices}")
        
#         device = devices[0]
#         print(device)
#     else:
#         print("No devices")
#         device = EmailDevice.objects.create(
#             user=instance,
#             email=email,
#             name='Primary Email',
#             confirmed=True
#         )
#         print("Email Device created")

#     device.generate_challenge()
#     message = f"Your login code is {device.token}"
#     send_mail(
#         "SJLSHS Login Code",
#         message,
#         from_email="SJLSHS@gmail.com",
#         recipient_list=[email],
#         fail_silently=False,
#     )
#     print("OTP Sent to mail")


# @receiver(user_logged_in)
# def send_login_code(sender, request, user, **kwargs):
#     devices = list(devices_for_user(user))
#     if devices:
#         device = devices[0]
#         device.generate_challenge()
#         message = f"Your login code is {device.token}"
#         send_mail(
#             "SJLSHS Login Code",
#             message,
#             from_email="SJLSHS@gmail.com",
#             recipient_list=[user.email],
#             fail_silently=False,
#         )