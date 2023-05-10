from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from saintsite.crawl_saint import get_saint_cookies, pretty_print_takes_info, get_takes_info, get_student_info
from saintsite.crawl_courses import crawl_courses
#from .forms import StudentForm


def my_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cookies = get_saint_cookies(username, password)
        if get_student_info(cookies) == None:
            return render(request, 'logins.html')
        user = authenticate(username=username)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            #form = StudentForm(request.POST)
            #form.save()
            return redirect('home')
    else:
        # GET 요청 처리
        pass
    return render(request, 'logins.html')

