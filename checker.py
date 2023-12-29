from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from absence_file_parser import parse_absent_days
from date_utils import is_in_date_window
from result_reporter import report_result

# Five years’ continuous residence means that for 5 years in a row you’ve been in the UK, the Channel Islands or the Isle of Man for at least 6 months in any 12-month period.
# https://www.gov.uk/settled-status-eu-citizens-families/what-settled-and-presettled-status-means

# You must only include whole days in this calculation. Part day absences, for example, less than 24 hours, are not counted.
# https://www.gov.uk/government/publications/indefinite-leave-to-remain-calculating-continuous-period-in-uk/indefinite-leave-to-remain-calculating-continuous-period-in-uk-accessible

print('CONTINUOUS RESIDENCE CHECKER')

all_absent_days = parse_absent_days()

window_start = min(all_absent_days)
window_end = window_start + relativedelta(years=1)

absent_days_running_count = sum(1 for absent_day in all_absent_days if is_in_date_window(window_start, window_end, absent_day))

max_absent_days_count = absent_days_running_count
max_count_window_start = window_start
max_count_window_end = window_end
past_year_absent_days_count = 0

today = datetime.today().date()
end_date = max(max(all_absent_days), today)

while window_end <= end_date:
    if window_start in all_absent_days:
        absent_days_running_count -= 1

    if window_end in all_absent_days:
        absent_days_running_count += 1

    window_start += relativedelta(days=1)
    window_end += relativedelta(days=1)

    if absent_days_running_count >= max_absent_days_count:
        max_absent_days_count = absent_days_running_count
        max_count_window_start = window_start
        max_count_window_end = window_end
    
    if window_end == today:
        past_year_absent_days_count = absent_days_running_count

report_result('Max', max_absent_days_count, max_count_window_start, max_count_window_end)
print()
report_result('Past year', past_year_absent_days_count, today - relativedelta(years=1), today)