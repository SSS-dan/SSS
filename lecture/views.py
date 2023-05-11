from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from pybo.models import *


def lecture_list(request):
    times = ['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00']
    # days 리스트 정의
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    # lectures 쿼리셋 객체 생성
    user = request.user
    print(user.username)
    lectures = Student.get_takes(user.username).course
    context = {'lectures':lectures, 'times': times, 'days': days}
    return render(request, 'timetable.html', context)


def lecture_detail(request, lecture_id):
    lecture = Course.get_course_by_id(lecture_id)
    return render(request, 'lecture_detail.html', {'lecture': lecture})


@login_required
def lecture_new(request):
    print(request.user)
    if request.method == 'POST':
        print(request.POST)
        form = Course(course_id = None, semester = 3, name = request.POST['name'], day = request.POST['day'], start_time = request.POST['start_time'], end_time = request.POST['end_time'], classroom = request.POST['classroom'], advisor = request.POST['advisor'], major=None)
        #form.student = Student.get_student_by_id(request.user.username)
        #if form.is_valid():
        form.save()
        lecture = Takes(student = Student.get_student_by_id(request.user.username),course=form,middle_grade=None, final_grade = None, real=False)
        print(123)
        return redirect('timetable')
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
