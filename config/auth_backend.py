from django.contrib.auth.backends import ModelBackend
from qr_app.models import NewUser

User_model = NewUser

class PasswordlessAuthBackend(ModelBackend):
    """Log in to Django without providing a password.

    """
    def authenticate(self, username=None):
        print(123)
        try:
            user = User_model.objects.get(username=username)
            print("이미 있음")
        except User_model.DoesNotExist:
            user = User_model(username=username)
            user.save()
        return user


    def get_user(self, user_id):
        try:
            return User_model.objects.get(pk=user_id)
        except User_model.DoesNotExist:
            return None