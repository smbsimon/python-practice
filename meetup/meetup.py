from datetime import date
import calendar

def meetup_day(year, month, weekday, attribute):
    days_of_the_week = [i for i in calendar.day_name]
    weekday_index = days_of_the_week.index(weekday)

    month_split_by_weeks = calendar.monthcalendar(year, month)

    if attribute == 'last':
        week_index = -1
    elif attribute == 'teenth':
        week_index = 2
        if zip(*month_split_by_weeks)[weekday_index][2] <= 12:
            week_index = 3
    else:
        week_index = int(attribute[0])
        if month_split_by_weeks[0][weekday_index] != 0:
            week_index = week_index - 1

    day = month_split_by_weeks[week_index][weekday_index]

    return date(year, month, day)
