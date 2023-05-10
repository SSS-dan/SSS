from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lecture
from .forms import LectureForm
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from models import *

def lecture_list(request):
    lectures = Lecture.objects.all()
    times = ['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00']
    # days 리스트 정의
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    # lectures 쿼리셋 객체 생성
    user = request.user
    lectures = Lecture.objects.filter(user=user)
    context = {'lectures':lectures, 'times': times, 'days': days}
    return render(request, 'timetable.html', context)

def lecture_detail(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    return render(request, 'lecture_detail.html', {'lecture': lecture})

@login_required
def lecture_new(request):
    print(request.user)
    if request.method == 'POST':
        form = LectureForm(request.POST)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.user_id = request.user  # 로그인한 사용자의 정보로 채워줌
            lecture.save()
            return redirect('timetable')
    else:
        form = LectureForm()
    return render(request, 'lecture/create.html', {'form': form})

def lecture_edit(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    if request.method == 'POST':
        form = LectureForm(request.POST, instance=lecture)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.save()
            return redirect('lecture_detail', lecture_id=lecture.pk)
    else:
        form = LectureForm(instance=lecture)
    return render(request, 'lecture_edit.html', {'form': form})

def lecture_delete(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    lecture.delete()
    return redirect('lecture_list')
