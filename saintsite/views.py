from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def my_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # 로그인 실패 처리
            pass
    else:
        # GET 요청 처리
        pass
    return render(request, 'login.html')

