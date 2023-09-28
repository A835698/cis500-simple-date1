#######################################################
# my_date
#
# Name: (Avinash Ponnada)
# Section: 03
#
# Fall 2023
#########################################################


def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year, False otherwise"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False

 
def ordinal_date(year:int , month: int, day: int) -> int:
    """ Return the number of days elapsed since the beginning of the year, including any partial days.
        For example, the ordinal date for 1 January is 1.
        Hint: pre-compute the ordinal date for the first of each month."""
    day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #in leap year (February has 29 days)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        day_in_month[2] = 29
    ordinal = day
    for i in range(1, month):
        ordinal += day_in_month[i]

    return ordinal


def days_elapsed(year1: int, month1: int, day1: int, year2: int, month2: int, day2:int ) -> int:
    """ Return the number of days that have elapsed between year1-month1-day1 and year2-month2-day2.
        You may assume that year1-month1-day1 falls on or before year2-month2-day2. (In other words,
        your answer will always be >= 0.) """
    import datetime
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    diff = date2 - date1
    return diff.days

# This is a tuple. It is immutable so that users can't accidentally modify it.
DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def day_of_week(year: int, month: int, day: int) -> str:
    """ Return the day of the week (Sunday, Monday, Tuesday, etc.) for the given day
        Hint 1: 1 January 1753 was a Monday.
        Hint 2: Use the methods you've already written."""
    import datetime
    date_object = datetime.date(year, month, day)
    index = date_object.weekday()
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days_of_week[index]
    
def to_str(year: int, month: int, day: int) -> str:
    """ Return this date as string of the form "Wednesday, 07 March 1833"."""
    import datetime
    date_object = datetime.date(year, month, day)
    str_date = date_object.strftime("%A, %d %B %Y")
    return str_date

              
    