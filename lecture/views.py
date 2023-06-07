from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from pybo.models import *
from datetime import datetime,time
from users.models import User
import json

def lecture_list(request):
    user = request.user
    #print(user.student_id)
    lectures = User.get_takes(user.student_id)
    value = '231'
    if request.method == 'POST':
        value = request.POST['value']
        #print(value)
    runtime = []
    time = []
    day = []
    adv = []
    lname = []
    lplace = []
    lecture = []
    lec_id = []
    real = []
    advi = []
    for i in lectures.all():
        if i.course.semester == int(value):
            et = i.course.end_time
            st = i.course.start_time
            runtime.append(((et.hour-st.hour)*60+et.minute-st.minute)*1.083333333333333)
            #print(((st.hour-9)*60+st.minute)*1.083333333333333)
            time.append(((st.hour-9)*60+st.minute)*1.083333333333333)
            day.append(i.course.day)
            adv.append(i.course.advisor)
            lname.append(i.course.name)
            lplace.append(i.course.classroom)
            if i.real: real.append(1)
            else: real.append(0)
    lec = Course.objects.filter(semester = '231')
    for i in lec.all():
        lecture.append(i.name)
        lec_id.append(i.course_id)
        advi.append(i.advisor)
    context = {'semester' : value, 'runtime' : runtime, 'time' : time, 'day' : day, 'adv' : json.dumps(adv), 'lname' : json.dumps(lname), 'lplace' : json.dumps(lplace), 'lecture': json.dumps(lecture), 'lec_id': json.dumps(lec_id), 'real':real, 'advi': json.dumps(advi)}    #context = {'lectures' : lec,'times': times, 'days': days}
    return render(request, 'timetable.html', context)


def lecture_select(request, lecture_id):
    print(lecture_id)
    lec = Course.get_course_by_id(lecture_id, 231)
    takes=User.get_takes(request.user.student_id)
    for i in takes.all():
        if i.course.semester == lec.semester:
            if i.course.day % 10 == lec.day % 10 or i.course.day / 10 == lec.day % 10 or i.course.day % 10 == lec.day / 10 or i.course.day / 10 == lec.day / 10:
                if i.course.start_time < lec.end_time and i.course.start_time >= lec.start_time:
                    return redirect('lecture_list')
                if i.course.end_time <= lec.end_time and i.course.end_time > lec.start_time:
                    return redirect('lecture_list')
    lecture = Takes()
    lecture.student = User.get_student_by_id(request.user.student_id)
    print(lec)
    lecture.course=lec
    lecture.middle_grade=None
    lecture.final_grade = None
    lecture.real=True
    lecture.save()
    return redirect('lecture_list')

daytoint = {'월요일':1, '화요일':2, '수요일':3, '목요일':4, '금요일':5, '토요일':6, '일요일':7}
@login_required
def lecture_new(request,name,advisor,classroom,day,start_time,end_time):
    print(request.user)
    form = Course()
    form.course_id = None
    form.semester = 231
    form.name = name
    form.day = daytoint[day]
    form.start_time = datetime.strptime(start_time,"%H:%M").time()
    form.end_time = datetime.strptime(end_time,"%H:%M").time()
    form.classroom = classroom
    form.advisor = advisor
    form.major=None
    takes=User.get_takes(request.user.student_id)
    for i in takes.all():
        if i.course.semester == form.semester:
            if i.course.day % 10 == form.day % 10 or (int)(i.course.day / 10) == form.day % 10 or i.course.day % 10 == form.day / 10 or (int)(i.course.day / 10) == form.day / 10:
                if i.course.start_time < form.end_time and i.course.start_time >= form.start_time:
                    return redirect('lecture_list')
                if i.course.end_time <= form.end_time and i.course.end_time > form.start_time:
                    return redirect('lecture_list')
    form.save()
    lecture = Takes()
    lecture.student = User.get_student_by_id(request.user.student_id)
    lecture.course=form
    lecture.middle_grade=None
    lecture.final_grade = None
    lecture.real=False
    lecture.save()
    return redirect('lecture_list')


def lecture_edit(request, lecture_id,name,advisor,classroom,day,start_time,end_time):
    take = User.get_takes(request.user.student_id)
    form = Course()
    form.course_id = None
    form.semester = 231
    form.name = name
    form.day = daytoint[day]
    form.start_time = datetime.strptime(start_time,"%H:%M").time()
    form.end_time = datetime.strptime(end_time,"%H:%M").time()
    form.classroom = classroom
    form.advisor = advisor
    form.major=None
    takes=User.get_takes(request.user.student_id)
    for i in takes.all():
        if take.all()[int(lecture_id)].course.day == i.course.day and take.all()[int(lecture_id)].course.start_time == i.course.start_time and take.all()[int(lecture_id)].course.end_time == i.course.end_time : continue
        print(i.course.name)
        if i.course.semester == form.semester:
            print(i.course.day)
            if i.course.day % 10 == form.day % 10 or (int)(i.course.day / 10) == form.day % 10 or i.course.day % 10 == form.day / 10 or (int)(i.course.day / 10) == form.day / 10:
                print(i.course.name)
                if i.course.start_time < form.end_time and i.course.start_time >= form.start_time:
                    return redirect('lecture_list')
                if i.course.end_time <= form.end_time and i.course.end_time > form.start_time:
                    return redirect('lecture_list')
    form.save()
    lecture = Takes()
    take.all()[int(lecture_id)].delete()
    lecture.student = User.get_student_by_id(request.user.student_id)
    lecture.course=form
    lecture.middle_grade=None
    lecture.final_grade = None
    lecture.real=False
    lecture.save()
    return redirect('lecture_list')



def lecture_delete(request, lecture_id):
    user = request.user
    lectures = User.get_takes(user.student_id)
    lectures.all()[int(lecture_id)].delete()
    #lecture = Course.get_course_by_id(lecture_id,231)
    #lecture.delete()
    return redirect('lecture_list')
