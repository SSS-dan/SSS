from apscheduler.schedulers.background import BackgroundScheduler

def get_current_courses():
  print(123) #반복되는 함수

def run():
    sched = BackgroundScheduler()
    sched.add_job(get_current_courses,'interval', seconds=3, id='test')
    sched.start()