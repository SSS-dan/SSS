from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from pybo.models import *
from datetime import datetime,time


def lecture_list(request):
    times = ['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00']
    for i in range(len(times)):
        times[i] = datetime.strptime(times[i], '%H:%M').time()
    # days 리스트 정의
    days = [0 , 1, 2, 3, 4]
    # lectures 쿼리셋 객체 생성
    user = request.user
    print(user.username)
    lectures = Student.get_takes(user.username)
    lec = []
    for i in lectures.all():
        temp = {}
        temp['day'] = 1
        temp['start_time'] = i.course.start_time
        temp['end_time'] = i.course.end_time
        temp['name'] = i.course.name
        lec.append(temp)
    context = {'lectures' : lec,'times': times, 'days': days}
    return render(request, 'timetable.html', context)


def lecture_detail(request, lecture_id):
    lecture = Course.get_course_by_id(lecture_id)
    return render(request, 'lecture_detail.html', {'lecture': lecture})


@login_required
def lecture_new(request):
    print(request.user)
    if request.method == 'POST':
        #print(request.POST['name'])
        form = Course()
        form.course_id = None
        form.semester = 3
        form.name = request.POST['name']
        form.day = request.POST['day']
        form.start_time = request.POST['start_time']
        form.end_time = request.POST['end_time']
        form.classroom = request.POST['classroom']
        form.advisor = request.POST['advisor']
        form.major=None
        #form.student = Student.get_student_by_id(request.user.username)
        #if form.is_valid():
        print(form)
        form.save()
        lecture = Takes()
        lecture.student = Student.get_student_by_id(request.user.username)
        lecture.course=form
        lecture.middle_grade=None
        lecture.final_grade = None
        lecture.real=False
        lecture.save()
        print(123)
        return redirect('lecture_list')
    else:
        form = Takes()
    return render(request, 'lecture/create.html', {'form': form})

def lecture_select(request):
    if request.method is 'POST':
        form = Takes(request.POST)
        form.semester = 2124
        form.student = request.user.username
        form.real = True
        #if form.is_valid():
        lecture = form.save(commit=False)
        lecture.save()
        return redirect('timetable')
    else:
        form = Takes()
    return render(request, 'lecture_select.html', {'form':form})


def lecture_edit(request, lecture_id):
    lecture = Course.get_course_by_id(lecture_id)
    if request.method == 'POST':
        form = Course(request.POST) 
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.save()
            return redirect('lecture_detail', lecture_id=lecture.course_id)
    else:
        return render(request, 'lecture_edit.html', {'form': form})


def lecture_delete(request, lecture_id):
    lecture = Course.get_course_by_id(lecture_id)
    lecture.delete()
    return redirect('lecture_list')
