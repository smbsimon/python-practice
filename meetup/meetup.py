import datetime
import calendar
import re

def meetup_day(year, month, weekday, attribute):

    dayz = {'Monday' : 0, 'Tuesday' : 1, 'Wednesday' : 2, 'Thursday' : 3, 'Friday' : 4, 'Saturday' : 5, 'Sunday' : 6}
    split_month = calendar.monthcalendar(year, month)
    attribute = int(re.sub(r'\D', "", attribute))

    all_of_same_weekday = []

    for i in range(7):
        all_of_same_weekday.append([row[i] for row in split_month])

    weekday_by_number = dayz[weekday]

    if all_of_same_weekday[weekday_by_number][0] > 0:
        attribute = attribute - 1

    date = all_of_same_weekday[weekday_by_number][attribute]

    return datetime.date(year, month, date)
