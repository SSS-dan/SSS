from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from pybo.models import *
from datetime import datetime,time
from users.models import User


def lecture_list(request):
    times = ['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00']
    for i in range(len(times)):
        times[i] = datetime.strptime(times[i], '%H:%M').time()
    # days 리스트 정의
    days = [0 , 1, 2, 3, 4]
    # lectures 쿼리셋 객체 생성
    user = request.user
    print(user.student_id)
    lectures = User.get_takes(user.student_id)
    lec = []
    for i in lectures.all():
        temp = {}
        temp['day'] = i.course.day
        temp['start_time'] = i.course.start_time
        temp['end_time'] = i.course.end_time
        temp['name'] = i.course.name
        lec.append(temp)
    context = {'lectures' : lec,'times': times, 'days': days}
    return render(request, 'timetable.html', context)


def lecture_detail(request, lecture_id):
    print(lecture_id)
    lec = Course.get_course_by_id(lecture_id, 231)
    lecture = Takes()
    lecture.student = User.get_student_by_id(request.user.student_id)
    print(lec)
    lecture.course=lec
    lecture.middle_grade=None
    lecture.final_grade = None
    lecture.real=False
    lecture.save()
    return redirect('lecture_list')

@login_required
def lecture_new(request):
    print(request.user)
    if request.method == 'POST':
        #print(request.POST['name'])
        form = Course()
        form.course_id = None
        form.semester = 231
        form.name = request.POST['name']
        form.day = request.POST['day']
        form.start_time = request.POST['start_time']
        form.end_time = request.POST['end_time']
        form.classroom = request.POST['classroom']
        form.advisor = request.POST['advisor']
        form.major=None
        if form.is_valid():
            form.save()
            lecture = Takes()
            lecture.student = User.get_student_by_id(request.user.student_id)
            lecture.course=form
            lecture.middle_grade=None
            lecture.final_grade = None
            lecture.real=False
            if lecture.is_valid():
                lecture.save()
            #else :
        #else :
        return redirect('lecture_list')
    else:
        form = Takes()
    return render(request, 'lecture/create.html', {'form': form})

def lecture_select(request):
    form = Course.objects.all()
    lec = []
    for i in form.all():
        if i.course_id is not None :
            temp = {}
            temp['day'] = i.day
            temp['start_time'] = i.start_time
            temp['end_time'] = i.end_time
            temp['name'] = i.name
            temp['id']=i.course_id
            lec.append(temp)
    if request.method == 'POST':
        return redirect('lecture_list')
    else:
        form = Course.objects.all()
    return render(request, 'lecture_select.html', {'lectures':lec})


def lecture_edit(request, lecture_id):
    lecture = Course.get_course_by_id(lecture_id,231)
    if request.method == 'POST':
        form = Course(request.POST) 
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.save()
            return redirect('lecture_detail', lecture_id=lecture.course_id)
    else:
        return render(request, 'lecture_edit.html', {'form': form})


def lecture_delete(request, lecture_id):
    #lecture = Course.get_course_by_id(lecture_id,231)
    #lecture.delete()
    return redirect('lecture_list')
