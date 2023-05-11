from django.urls import path
from qr_app import views as qr_app

app_name = 'pybo'

urlpatterns = [
    path('', qr_app.mainpage),
]