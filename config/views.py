from django.shortcuts import render, redirect
from .crawl_saint import get_saint_cookies, pretty_print_takes_info, get_takes_info, get_student_info
from .crawl_courses import crawl_courses
<<<<<<< HEAD
from qr_app.models import NewUser
from .auth_backend import PasswordlessAuthBackend
=======
from qr_app.forms import RegisterForm

>>>>>>> 4accb2587f8599915fee1f7e8ba0cfb5a6b73851

def my_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cookies = get_saint_cookies(username, password)
        if get_student_info(cookies) == None:
            return render(request, 'logins.html')
<<<<<<< HEAD
        user = PasswordlessAuthBackend().authenticate(username=username)
        print(user)
        PasswordlessAuthBackend().login(request, user)
=======
        user = authenticate(username=username)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form = RegisterForm(username=username)
            form.save()
            return redirect('home')
>>>>>>> 4accb2587f8599915fee1f7e8ba0cfb5a6b73851
    else:
        # GET 요청 처리
        pass
    return render(request, 'logins.html')

