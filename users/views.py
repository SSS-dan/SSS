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
from users.models import User, UserProfile
from django.shortcuts import render, redirect
from .forms import UserProfileForm


def upload_profile_picture(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            try:
                what = UserProfile.objects.get(user=request.user)
            except user_profile.DoesNotExist:
                user_profile.save()
                pass
            else:
                what.profile_picture = user_profile.profile_picture
                what.save()
                pass

            return redirect('home')
    else:
        form = UserProfileForm()
    return render(request, 'upload_profile_picture.html', {'form': form})


def setting(request):
    context = {
        'username': request.user.student_id,
        'student': User.objects.get(student_id=request.user.student_id),
    }
    return render(request, 'setting.html', context=context)


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
        image_bytes = generate_qr_code(request.user.student_id)
        context = {
            'username': request.user.student_id,
            'student': User.objects.get(student_id=request.user.student_id),
            'qr_code': 'data:image/png;base64,' + base64.b64encode(image_bytes).decode()
        }
        # print(crawl_courses('23', '1'))
        return render(request, 'qr_code.html', context=context)
    return render(request, 'index.html')


def mainpage(request):
    user = request.user
    if user.is_authenticated:
        image_bytes = generate_qr_code(request.user.student_id)
        context = {
            'username': request.user.student_id,
            'student': User.objects.get(student_id=request.user.student_id),
            'qr_code': 'data:image/png;base64,' + base64.b64encode(image_bytes).decode(),
            'notices': Notice.objects.all().order_by('-id')[:5],
        }
        return render(request, 'index.html', context=context)
    else:
        return render(request, 'index.html')
