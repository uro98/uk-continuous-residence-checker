import argparse
from dateutil.relativedelta import relativedelta
from date_utils import to_date

def parse_args():
    parser = argparse.ArgumentParser(description='Check dates are within the specified limit in a 12-month rolling window.')
    parser.add_argument('file_name', help='name of the file containing dates')
    parser.add_argument('limit', help='limit to check against', type=int)
    parser.add_argument('-v', '--verbose', action='store_true', help="print days running count")
    return parser.parse_args()

def parse_file_dates(file_name):
    # File format: one period (e.g. 2023/1/15 - 2023/1/22) per line, both dates are included

    file = open(file_name, 'r')
    periods = file.readlines() 

    days = set()

    for period in periods:
        start_date = to_date(period.split(' - ')[0])
        end_date = to_date(period.split(' - ')[1].strip())

        period_length = (end_date - start_date).days + 1

        for i in range(0, period_length):
            day = (start_date + relativedelta(days=i)).date()
            days.add(day)

    return days