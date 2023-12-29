from dateutil.relativedelta import relativedelta
from date_utils import to_date

# absences.txt format: one absence period (e.g. 2023/1/15 - 2023/1/22) per line

def parse_absent_days():
    absence_file = open('absences.txt', 'r')
    absence_periods = absence_file.readlines()

    absent_days = set()

    for absence_period in absence_periods:
        departure_day = to_date(absence_period.split(' - ')[0])
        return_day = to_date(absence_period.split(' - ')[1].strip())

        trip_length = (return_day - departure_day).days

        for i in range(1, trip_length):
            absent_days.add((departure_day + relativedelta(days=i)).date())

    return absent_days