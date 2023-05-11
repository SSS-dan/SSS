from django.shortcuts import render, redirect
from .crawl_saint import get_saint_cookies, pretty_print_takes_info, get_takes_info, get_student_info
from .crawl_courses import crawl_courses
from qr_app.models import NewUser
from .auth_backend import PasswordlessAuthBackend
from django.contrib.auth import login as auth_login

def my_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cookies = get_saint_cookies(username, password)
        if get_student_info(cookies) is None:
            return render(request, 'logins.html')
        user = PasswordlessAuthBackend().authenticate(username=username)
        print(user)
        # login 함수 호출
        auth_login(request, user)
        return redirect('qr_app:qr_code')
    else:
        # GET 요청 처리
        pass
    return render(request, 'logins.html')

