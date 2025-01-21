from date_utils import to_string

def print_result(days_count, start_date, end_date, limit):
    days_to_limit = limit - days_count

    print('{} days '.format(days_count), end='')
    print('({} day{} {} {} day limit)'.format(abs(days_to_limit), 's' if abs(days_to_limit) != 1 else '', 'under' if days_to_limit >= 0 else 'over', limit))
    print('From {} (inclusive) to {} (exclusive)'.format(to_string(start_date), to_string(end_date)))