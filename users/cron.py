from apscheduler.schedulers.background import BackgroundScheduler
from config.crawl_courses import crawl_courses
from pybo.models import *
from datetime import datetime,time

daytoint = {'월':0, '화':1, '수':2, '목':3, '금':4, '토':5, '일':6}

def get_current_courses():
  #반복되는 함수 course를 받아와서 데이터베이스에 저장해줌
  print(2134)
  crawls = crawl_courses('23','1')
  print(crawls)
  if crawls is not None :
    for i in range(len(crawls)) :
        course = Course.get_course_by_id(crawls['과목번호'][i],231)
        if course is None :
          course = Course()
        course.advisor = crawls['교수진'][i]
        course.classroom = crawls['강의실'][i]
        course.course_id = crawls['과목번호'][i]
        #print(crawls['요일1'][i])
        if len(crawls['요일1'][i]) == 0 or len(crawls['요일1'][i])>5:
           day = 7
        else :
           day = daytoint[crawls['요일1'][i].split(',')[0]]
        course.day = day
        if len(crawls['종료시간1'][i]) == 0 :
          course.end_time = datetime.strptime('09:00', '%H:%M').time()
          course.start_time = datetime.strptime('09:00', '%H:%M').time()
        else :
          course.end_time = datetime.strptime(crawls['종료시간1'][i], '%H:%M').time()
          course.start_time = datetime.strptime(crawls['시작시간1'][i], '%H:%M').time()
        course.name = crawls['과목명'][i]
        course.semester = 231
        course.save()


def run():
    get_current_courses()
    sched = BackgroundScheduler()
    sched.add_job(get_current_courses,'interval', seconds=300000, id='test')
    sched.start()
    pass