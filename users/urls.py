from django.urls import path
from .views import qr_code
from .views import upload_profile_picture

urlpatterns = [
    path('upload-profile-picture/', upload_profile_picture, name='upload_profile_picture'),
    path('', qr_code, name='qr_code'),
]
