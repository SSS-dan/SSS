from apscheduler.schedulers.background import BackgroundScheduler
from config.crawl_courses import crawl_courses
from pybo.models import *

def get_current_courses():
  #반복되는 함수 course를 받아와서 데이터베이스에 저장해줌
  print(2134)
  crawls = crawl_courses('23','1')
  for crawl in crawls :
    course = Course.get_course_by_id(crawl.id)
    if course is None :
      course = Course()
      course.advisor = crawl.advisor
      course.classroom = crawl.classroom
      course.course_id = crawl.id
      course.day = int(crawl.day)
      course.end_time = crawl.end_time
      course.start_time = crawl.start_time
      course.name = crawl.name
      course.semester = 1
    course.save()


def run():
    #get_current_courses()
    #sched = BackgroundScheduler()
    #sched.add_job(get_current_courses,'interval', seconds=300000, id='test')
    #sched.start()
    pass