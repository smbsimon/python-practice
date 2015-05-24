import datetime
import calendar
import re

def meetup_day(year, month, weekday, attribute):

    dayz = {'Monday' : 0, 'Tuesday' : 1, 'Wednesday' : 2, 'Thursday' : 3, 'Friday' : 4, 'Saturday' : 5, 'Sunday' : 6}
    split_month = calendar.monthcalendar(year, month)
    weekday_number = dayz[weekday]

    same_weekday = []

    for i in range(7):
        same_weekday.append([row[i] for row in split_month])

    if any(char.isdigit() for char in attribute):
        attribute = int(re.sub(r'\D', "", attribute))
        if same_weekday[weekday_number][0] > 0:
            attribute = attribute - 1
        date = same_weekday[weekday_number][attribute]
    elif attribute == 'last':
        date = same_weekday[weekday_number][-1]
    elif attribute == 'teenth':
        for i in same_weekday[weekday_number]:
            if i >= 13:
                date = i
                break

    return datetime.date(year, month, date)
