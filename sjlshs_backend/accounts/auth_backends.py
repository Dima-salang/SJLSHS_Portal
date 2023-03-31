from django.contrib.auth.backends import BaseBackend, ModelBackend
from django.contrib.auth import get_user_model
from django_otp.plugins.otp_email.models import EmailDevice
from django_otp import devices_for_user

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, otp_token=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
            devices = devices_for_user(user)
            if not devices:
                return None
            for device in devices:
                if device.confirmed and device.verify_token(otp_token) and device.user == user:
                    return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None