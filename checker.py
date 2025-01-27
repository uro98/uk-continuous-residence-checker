from datetime import datetime
from dateutil.relativedelta import relativedelta
from parser import parse_args, parse_file_dates
from date_utils import is_in_date_window
from result_printer import print_result

args = parse_args()
days = parse_file_dates(args.file_name)
today = datetime.today().date()

a_year_ago = today - relativedelta(years=1, days=1)
window_start = min(min(days), a_year_ago)
window_end = window_start + relativedelta(days=365)

days_running_count = sum(1 for day in days if is_in_date_window(window_start, window_end, day))

max_days_count = days_running_count
max_count_window_start = window_start
max_count_window_end = window_end

min_days_count = days_running_count
min_count_window_start = window_start
min_count_window_end = window_end

past_year_days_count = 0

end_date = max(max(days), today)

while window_end <= end_date:
    if window_start in days:
        days_running_count -= 1

    if window_end in days:
        days_running_count += 1

    window_start += relativedelta(days=1)
    window_end += relativedelta(days=1)

    if args.verbose:
        print('{} - {}: {}'.format(window_start, window_end, days_running_count))

    if days_running_count >= max_days_count:
        max_days_count = days_running_count
        max_count_window_start = window_start
        max_count_window_end = window_end

    if days_running_count < min_days_count:
        min_days_count = days_running_count
        min_count_window_start = window_start
        min_count_window_end = window_end
    
    if window_end == today:
        past_year_days_count = days_running_count

if args.verbose:
    print()

print('Max days count: ', end='')
print_result(max_days_count, max_count_window_start, max_count_window_end, args.limit)

print()
print('Min days count: ', end='')
print_result(min_days_count, min_count_window_start, min_count_window_end, args.limit)

print()
print('Past year days count: ', end='')
print_result(past_year_days_count, today - relativedelta(years=1), today, args.limit)