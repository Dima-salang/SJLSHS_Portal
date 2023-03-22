from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from accounts.models import StudentUser
from .models import *

@receiver(post_save, sender=FirstSem_1stQ)
def send_grade_update_email(sender, instance, **kwargs):
    print("Signal called")
    student_user = StudentUser.objects.get(lrn=instance.lrn)
    if kwargs.get('created', False):
        return
    subject = 'Grade Updated'
    message = f"""{instance.last_name}, {instance.first_name} - {instance.lrn}
                  Your grade is uploaded:
                  PR2: {instance.PR2}
                  CPAR: {instance.CPAR}
                  PHILOSOPHY: {instance.PHILOSOPHY}
                  UCSP: {instance.UCSP}
                  EAPP: {instance.EAPP}
                  SPECIALIZED: {instance.SPECIALIZED}
                  SPECIALIZED: {instance.SPECIALIZED}
                  PE: {instance.PE}
                  Average: {instance.Average}
                  """
    email_from = "SJLSHS@gmail.com"
    recipient_email = student_user.email
    recipient_list = [recipient_email]
    send_mail(subject, message, email_from, recipient_list)
    print(f"Email sent to {recipient_list}")


@receiver(post_save, sender=FirstSem_2ndQ)
def send_grade_update_email(sender, instance, **kwargs):
    print("Signal called")
    student_user = StudentUser.objects.get(lrn=instance.lrn)
    if kwargs.get('created', False):
        return
    subject = 'Grade Updated'
    message = f"""{instance.last_name}, {instance.first_name} - {instance.lrn}
                  Your grade is uploaded:
                  PR2: {instance.PR2}
                  CPAR: {instance.CPAR}
                  PHILOSOPHY: {instance.PHILOSOPHY}
                  UCSP: {instance.UCSP}
                  EAPP: {instance.EAPP}
                  SPECIALIZED: {instance.SPECIALIZED}
                  SPECIALIZED: {instance.SPECIALIZED}
                  PE: {instance.PE}
                  Average: {instance.Average}
                  """
    email_from = "SJLSHS@gmail.com"
    recipient_email = student_user.email
    recipient_list = [recipient_email]
    send_mail(subject, message, email_from, recipient_list)
    print(f"Email sent to {recipient_list}")


@receiver(post_save, sender=SecondSem_3rdQ)
def send_grade_update_email(sender, instance, **kwargs):
    print("Signal called")
    student_user = StudentUser.objects.get(lrn=instance.lrn)
    if kwargs.get('created', False):
        return
    subject = 'Grade Updated'
    message = f"""{instance.last_name}, {instance.first_name} - {instance.lrn}
                  Your grade is uploaded:
                  III: {instance.III}
                  MIL: {instance.MIL}
                  PE4: {instance.PE4}
                  IMMERSION: {instance.IMMERSION}
                  SPECIALIZED: {instance.SPECIALIZED}
                  SPECIALIZED: {instance.SPECIALIZED_2}
                  AVERAGE: {instance.Average}
                  """
    email_from = "SJLSHS@gmail.com"
    recipient_email = student_user.email
    recipient_list = [recipient_email]
    send_mail(subject, message, email_from, recipient_list)
    print(f"Email sent to {recipient_list}")


@receiver(post_save, sender=SecondSem_4thQ)
def send_grade_update_email(sender, instance, **kwargs):
    print("Signal called")
    student_user = StudentUser.objects.get(lrn=instance.lrn)
    if kwargs.get('created', False):
        return
    subject = 'Grade Updated'
    message = f"""{instance.last_name}, {instance.first_name} - {instance.lrn}
                  Your grade is uploaded:
                  III: {instance.III}
                  MIL: {instance.MIL}
                  PE4: {instance.PE4}
                  IMMERSION: {instance.IMMERSION}
                  SPECIALIZED: {instance.SPECIALIZED}
                  SPECIALIZED: {instance.SPECIALIZED_2}
                  AVERAGE: {instance.Average}
                  """
    email_from = "SJLSHS@gmail.com"
    recipient_email = student_user.email
    recipient_list = [recipient_email]
    send_mail(subject, message, email_from, recipient_list)
    print(f"Email sent to {recipient_list}")