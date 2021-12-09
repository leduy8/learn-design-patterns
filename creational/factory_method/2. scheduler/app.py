from scheduler import Scheduler
from arabian_scheduler import ArabianScheduler
from event import Event

scheduler = Scheduler()
scheduler.schedule(Event("big night"))


a_scheduler = ArabianScheduler()
a_scheduler.schedule(Event("another big night"))