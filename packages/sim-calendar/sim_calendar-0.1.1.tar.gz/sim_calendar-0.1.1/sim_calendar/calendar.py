from datetime import datetime, timedelta, MINYEAR
from sim_calendar.months import MONTHS

class Calendar:
    # Class to define a simple calendar for a time stepped simulation.
    # Mostly a wrapper for the datetime.datetime class, the smallest resolution 
    # is an hour. The values have ranges of the following:
    # Hour - 0 <= hour < 24
    # Day - 1 <= day <= # of days in the month
    # Month - 1 <= month <= 12
    # Year - MINYEAR (1) <= year <= MAXYEAR

    def __init__(self, startHour=0, startDay=1, startMonth=1, startYear=1, interval=1) -> None:
        # An interval of 1 indicates a step size of 1 hour, 2 is 2 hours, etc.
        self.tick = 0
        self.dt = datetime(year=startYear, month=startMonth, day=startDay, hour=startHour)
        self.interval = interval

    def fromDateTime(d: datetime, interval=1):
        # Construct a Calendar object from a datetime.datetime object
        cal = Calendar(startDay=d.day, startMonth=d.month, startYear=d.year, startHour=d.hour, interval=interval)
        return cal

    def DateTime(self) -> datetime:
        return self.dt

    def monthName(self) -> str:
        return MONTHS[self.month()-1]['name']

    def monthLength(self) -> int:
        return MONTHS[self.month()-1]['days']

    def hour(self) -> int:
        return self.dt.hour

    def day(self) -> int:
        return self.dt.day

    def month(self) -> int:
        return self.dt.month

    def year(self) -> int:
        return self.dt.year

    def step(self):
        self.tick += 1
        
        delta = timedelta(hours=self.interval)

        self.dt += delta

    def isNewDay(self) -> bool:
        return self.hour() == 0

    def isNewWeek(self) -> bool:
        return self.day() % 7 == 1

    def isNewMonth(self) -> bool:
        return self.day() == 1

    def isNewYear(self) -> bool:
        return self.day() == 1 and self.month() == 1

    def dayOfWeek(self) -> int:
        # Returns the day of the week from 0 to 6 where 0 is Monday
        return self.dt.weekday()