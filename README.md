# UK Continuous Residence Checker

Given a list of periods of dates, this tool calculates the number of days in rolling 12-month periods to check whether the maximum number is within a certain limit.

Example use cases:

- In the UK, to fulfill continuous residence requirements for settled status or indefinite leave to remain, residents need be in the UK for at least 6 months in any 12-month period, for 5 years in a row. Given a list of absences or trips away, this tool helps to check the 6-month limit will not be exceeded.
- Some companies allow employees to work abroad for up to 90 days in rolling 12-month periods. This tools helps plan time abroad without going over the 90-day limit.

## Usage

1. Clone the repository
2. Create a `.txt` file, and put in start (inclusive) and end (inclusive) dates for each period like so:
    ```
    2023/1/15 - 2023/1/22
    2023/3/24 - 2023/3/27
    2023/6/4 - 2023/7/16
    ```
3. In the same directory as `checker.py`, run the checker with `python checker.py [file_name] [limit]`
