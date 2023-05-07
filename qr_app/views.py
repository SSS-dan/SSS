import base64
import qrcode
import datetime as dt
from io import BytesIO
from PIL import Image
from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (iPod; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 \
        (KHTML, like Gecko) CriOS/87.0.4280.163 Mobile/15E148 Safari/604.1"
}

# request에 아이디 비번 암호 그대로 전달.. 서강대 보안 어데감?
LOGIN_INFO = {
    'destURL': '/',
    'userid': '2019XXXX',  # 니 학번
    'passwd': 'XXXXX',  # 니 비번
}

login_url = "https://msaint.sogang.ac.kr/loginproc.aspx"  # 모바일 세인트 로그인 주소


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
        #백엔드 : 세인트 아이디 비번이 맞는지
        LOGIN_INFO['userid']=request.POST.get('studentid')
        LOGIN_INFO['passwd']=request.POST.get('password')
        session = requests.session()  # 세션 만들어서 쿠키 값을 받아오자!
        response = session.post(login_url, headers=header, data=LOGIN_INFO, verify=False)
        cookies = response.cookies
        session.close()  # 세션 닫기

        # 세션을 닫았는데도! 저장된 쿠키 값 만으로 크롤링 성공
        print("Cookies received:")
        for cookie in cookies:
            print(f"{cookie.name}: {cookie.value}")
        #

        rsp = requests.get("https://msaint.sogang.ac.kr/grade/g2.aspx", cookies=cookies, verify=False)
        if rsp.status_code == 200:
            print("\n===========It worked!=========\n")
            # print(rsp.text)
            soup = BeautifulSoup(rsp.text, 'html.parser')
            # 수강신청 조회리스트를 추출
            courses = soup.select('tr[id^=tr]')

            # 수강신청 조회리스트를 순회하며 각 과목의 정보를 출력
            for course in courses:
                course_number = course.select_one('td:nth-child(1)').text
                course_class = course.select_one('td:nth-child(2)').text
                course_name = course.select_one('td:nth-child(3)').text
                print(f"과목번호: {course_number}, 분반: {course_class}, 교과목명: {course_name}")
        else:
            print(f"Request failed with status code {rsp.status_code}")
            return render(request, 'index.html')
        image_bytes = generate_qr_code(LOGIN_INFO['userid'])
        context = {'qr_code': 'data:image/png;base64,' + base64.b64encode(image_bytes).decode()}
        return render(request, 'qr_code.html', context=context)
    return render(request, 'index.html')