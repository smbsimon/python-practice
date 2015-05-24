import datetime
import calendar
import re

weekday_to_number = {weekday: number
    for (number, weekday) in enumerate(calendar.day_name)}

def meetup_day(year, month, weekday, attribute):

    month_split_by_weeks = calendar.monthcalendar(year, month)
    weekday_number = weekday_to_number[weekday]
    dates_split_by_weekdays = []

    for i in month_split_by_weeks:
        dates_split_by_weekdays = zip(*month_split_by_weeks)

    if any(char.isdigit() for char in attribute):
        attribute = int(re.sub(r'\D', "", attribute))
        if dates_split_by_weekdays[weekday_number][0] > 0:
            attribute = attribute - 1
        date = dates_split_by_weekdays[weekday_number][attribute]
    elif attribute == 'last':
        date = dates_split_by_weekdays[weekday_number][-1]
    elif attribute == 'teenth':
        for i in dates_split_by_weekdays[weekday_number]:
            if i >= 13:
                date = i
                break

    return datetime.date(year, month, date)
