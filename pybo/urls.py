from django.urls import path
from users import views as qr_app

app_name = 'pybo'

urlpatterns = [
    path('', qr_app.mainpage),
]