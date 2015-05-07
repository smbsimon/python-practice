def is_leap_year(year):
    return check_by_four_hundred(year) or check_by_one_hundred(year) and check_by_four(year)

def check_by_four_hundred(year):
    return year % 400 == 0

def check_by_one_hundred(year):
    return year % 100 != 0

def check_by_four(year):
    return year % 4 == 0
