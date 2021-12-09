from gregorian_calendar import GregorianCalendar
from datetime import date


class Scheduler:
    def __init__(self) -> None:
        self.calendar = self.create_calendar()

    def create_calendar(self):
        return GregorianCalendar()

    def schedule(self, event):
        today = date.today()
        self.calendar.add_event(event, today)