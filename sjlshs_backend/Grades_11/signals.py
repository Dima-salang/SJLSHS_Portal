from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from accounts.models import StudentUser
from .models import *


@receiver(post_save, sender=FirstSem_1stQ_11)
def send_grade_update_email(sender, instance, **kwargs):
    print("Signal called")
    student_user = StudentUser.objects.get(lrn=instance.lrn)
    if kwargs.get('created', False):
        return
    subject = 'Grade Updated'
    message = f"""{instance.last_name}, {instance.first_name} - {instance.lrn}
                  Your grade is uploaded:
                  ORAL COMMUNICATION: {instance.ORALCOMM}
                  KOMUNIKASYON AT PANANALIKSIK: {instance.KOMUNIKASYON}
                  GENERAL MATHEMATICS: {instance.GENMATH}
                  EARTH AND LIFE SCIENCE: {instance.ELS}
                  PERSONAL DEVELOPMENT: {instance.PERDEV}
                  SPECIALIZED: {instance.SPECIALIZED}
                  SPECIALIZED: {instance.SPECIALIZED_2}
                  PHYSICAL AND EDUCATION : {instance.PE}
                  Average: {instance.Average}
                  """
    email_from = "SJLSHS@gmail.com"
    recipient_email = student_user.email
    recipient_list = [recipient_email]
    send_mail(subject, message, email_from, recipient_list)
    print(f"Email sent to {recipient_list}")

@receiver(post_save, sender=FirstSem_2ndQ_11)
def send_grade_update_email(sender, instance, **kwargs):
    print("Signal called")
    student_user = StudentUser.objects.get(lrn=instance.lrn)
    if kwargs.get('created', False):
        return
    subject = 'Grade Updated'
    message = f"""{instance.last_name}, {instance.first_name} - {instance.lrn}
                  Your grade is uploaded:
                  ORAL COMMUNICATION: {instance.ORALCOMM}
                  KOMUNIKASYON AT PANANALIKSIK: {instance.KOMUNIKASYON}
                  GENERAL MATHEMATICS: {instance.GENMATH}
                  EARTH AND LIFE SCIENCE: {instance.ELS}
                  PERSONAL DEVELOPMENT: {instance.PERDEV}
                  SPECIALIZED: {instance.SPECIALIZED}
                  SPECIALIZED: {instance.SPECIALIZED_2}
                  PHYSICAL AND EDUCATION : {instance.PE}
                  Average: {instance.Average}
                  """
    email_from = "SJLSHS@gmail.com"
    recipient_email = student_user.email
    recipient_list = [recipient_email]
    send_mail(subject, message, email_from, recipient_list)
    print(f"Email sent to {recipient_list}")
























@receiver(post_save, sender=SecondSem_3rdQ_11)
def send_grade_update_email(sender, instance, **kwargs):
    print("Signal called")
    student_user = StudentUser.objects.get(lrn=instance.lrn)
    if kwargs.get('created', False):
        return
    subject = 'Grade Updated'
    message = f"""{instance.last_name}, {instance.first_name} - {instance.lrn}
                  Your grade is uploaded:
                  READING AND WRITING {instance.READING_WRITING}
                  PAGBASA {instance.PAGBASA}
                  STATISTICS AND PROBABILITY {instance.STATS_PROB}
                  PHYSICAL SCIENCE {instance.PHYSCI}
                  EMPOWERMENT TECHNOLOGIES {instance.EMPOWERMENT}
                  SPECIALIZED: {instance.SPECIALIZED}
                  SPECIALIZED: {instance.SPECIALIZED_2}
                  PHYSICAL AND EDUCATION 2: {instance.PE2}
                  Average: {instance.Average}
                  """
    email_from = "SJLSHS@gmail.com"
    recipient_email = student_user.email
    recipient_list = [recipient_email]
    send_mail(subject, message, email_from, recipient_list)
    print(f"Email sent to {recipient_list}")

@receiver(post_save, sender=SecondSem_4thQ_11)
def send_grade_update_email(sender, instance, **kwargs):
    print("Signal called")
    student_user = StudentUser.objects.get(lrn=instance.lrn)
    if kwargs.get('created', False):
        return
    subject = 'Grade Updated'
    message = f"""{instance.last_name}, {instance.first_name} - {instance.lrn}
                  Your grade is uploaded:
                  READING AND WRITING {instance.READING_WRITING}
                  PAGBASA {instance.PAGBASA}
                  STATISTICS AND PROBABILITY {instance.STATS_PROB}
                  PHYSICAL SCIENCE {instance.PHYSCI}
                  EMPOWERMENT TECHNOLOGIES {instance.EMPOWERMENT}
                  SPECIALIZED: {instance.SPECIALIZED}
                  SPECIALIZED: {instance.SPECIALIZED_2}
                  PHYSICAL AND EDUCATION 2: {instance.PE2}
                  Average: {instance.Average}
                  """
    email_from = "SJLSHS@gmail.com"
    recipient_email = student_user.email
    recipient_list = [recipient_email]
    send_mail(subject, message, email_from, recipient_list)
    print(f"Email sent to {recipient_list}")


