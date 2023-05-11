import base64
import qrcode
import datetime as dt
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from pybo.models import *
from config.crawl_courses import crawl_courses


def generate_qr_code(id):
    # QR 코드 생성
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    x = dt.datetime.now()
    data = id
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # 이미지 바이트로 변환
    buffer = BytesIO()
    img.save(buffer)
    image_bytes = buffer.getvalue()

    # Debugging
    print(f"generate_qr_code called with id: {id}, image_bytes length: {len(image_bytes)}")

    return image_bytes


def qr_code(request):
    if request.user.is_authenticated:
        image_bytes = generate_qr_code(request.user.username)
        context = {'qr_code': 'data:image/png;base64,' + base64.b64encode(image_bytes).decode()}
        # print(crawl_courses('23', '1'))
        return render(request, 'qr_code.html', context=context)
    return render(request, 'index.html')


def mainpage(request):
    # return render passing username
    image_bytes = generate_qr_code(request.user.username)
    context = {
        'username': request.user.username,

        'qr_code': 'data:image/png;base64,' + base64.b64encode(image_bytes).decode()
    }

    return render(request, 'index.html', context=context)
    # return render(request, 'index.html', {"username": request.user.username})
