from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from L_Autamation import send_love


sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_love, 'interval', seconds=5)

sched.start()