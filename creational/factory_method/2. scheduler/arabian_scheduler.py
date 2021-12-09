from arabian_calendar import ArabianCalendar
from scheduler import Scheduler


class ArabianScheduler(Scheduler):
    def create_calendar(self):
        return ArabianCalendar()