import base64
import qrcode
import datetime as dt
from io import BytesIO
from PIL import Image
from django.http import HttpResponse
from django.shortcuts import render

def generate_qr_code(id):
    # QR 코드 생성
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    x = dt.datetime.now()
    data = "_SG       "+id+'\n'+ str(x.year)+str(x.month)+str(x.day)+'\n'+str(x.hour).zfill(2)+'\n'+str(x.minute).zfill(2)+'\n'+str(x.second).zfill(2)+'\n'+str(int(x.microsecond/10)).zfill(5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # 이미지 바이트로 변환
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    image_bytes = buffer.getvalue()
    return image_bytes


def qr_code(request):
    if request.method == 'POST':
        student_id = request.POST.get('studentid')
        image_bytes = generate_qr_code(student_id)
        context = {'qr_code': 'data:image/png;base64,' + base64.b64encode(image_bytes).decode()}
        return render(request, 'qr_code.html', context=context)
    return render(request, 'index.html')