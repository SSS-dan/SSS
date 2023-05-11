import base64
import qrcode
import datetime as dt
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from pybo.models import *


def generate_qr_code(id):
    # QR 코드 생성
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    x = dt.datetime.now()
    qr.add_data(id)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # 이미지 바이트로 변환
    buffer = BytesIO()
    img.save(buffer)
    image_bytes = buffer.getvalue()
    return image_bytes


def qr_code(request):
    if request.method == 'POST':
        print(request.user)
        print(123)
        image_bytes = generate_qr_code(request.user.username)
        context = {'qr_code': 'data:image/png;base64,' + base64.b64encode(image_bytes).decode()}
        return render(request, 'qr_code.html', context=context)
    return render(request, 'index.html')