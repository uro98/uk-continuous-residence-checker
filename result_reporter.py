from date_utils import to_string

limit = 180

def report_result(type, absent_days_count, start_date, end_date):
    print('{} absent days count: {} '.format(type, absent_days_count), end='')
    days_to_limit = limit - absent_days_count
    print('({} day{} {} 180 day limit)'.format(abs(days_to_limit), 's' if abs(days_to_limit) != 1 else '', 'under' if days_to_limit >= 0 else 'over'))
    print('From {} (inclusive) to {} (exclusive)'.format(to_string(start_date), to_string(end_date)))