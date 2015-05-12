import datetime

def add_gigasecond(start_date):
    giga_difference = datetime.timedelta(seconds=1e9)
    end_date = start_date + giga_difference
    
    return end_date
