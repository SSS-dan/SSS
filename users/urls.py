from django.urls import path
from .views import qr_code
from .views import upload_profile_picture
from .views import setting

urlpatterns = [
    path('', qr_code, name='qr_code'),
    path('upload-profile-picture/', upload_profile_picture, name='upload_profile_picture'),
]
