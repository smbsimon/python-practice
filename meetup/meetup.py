import datetime
import calendar
import re

def meetup_day(year, month, weekday, attribute):
    days_of_the_week = [d for d in calendar.day_name]
    weekday_index = days_of_the_week.index(weekday)

    month_split_by_weeks = calendar.monthcalendar(year, month)
    dates_split_by_weekdays = []

    for i in month_split_by_weeks:
        dates_split_by_weekdays = zip(*month_split_by_weeks)

    if any(char.isdigit() for char in attribute):
        attribute = int(re.sub(r'\D', "", attribute))
        if dates_split_by_weekdays[weekday_index][0] > 0:
            attribute = attribute - 1
        date = dates_split_by_weekdays[weekday_index][attribute]
    elif attribute == 'last':
        date = dates_split_by_weekdays[weekday_index][-1]
    elif attribute == 'teenth':
        for i in dates_split_by_weekdays[weekday_index]:
            if i >= 13:
                date = i
                break

    return datetime.date(year, month, date)
