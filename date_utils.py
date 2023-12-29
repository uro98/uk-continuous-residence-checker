from datetime import datetime

date_format = '%Y/%m/%d'

def to_date(date_string):
    return datetime.strptime(date_string, date_format)

def to_string(date):
    return date.strftime(date_format)

def is_in_date_window(window_start_inclusive, window_end_exclusive, date):
    return window_start_inclusive <= date and date < window_end_exclusive