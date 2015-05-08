def is_leap_year(year):
    return divisible_by_four_hundred(year) or not_divisible_by_one_hundred(year) and divisible_by_four(year)

def divisible_by_four_hundred(year):
    return year % 400 == 0

def not_divisible_by_one_hundred(year):
    return year % 100 != 0

def divisible_by_four(year):
    return year % 4 == 0
