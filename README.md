# UK Continuous Residence Checker

Given a list of trips away from the UK, this tool calculates the number of absent days in all rolling 12 month periods to check whether continuous residence requirements for settled status or indefinite leave to remain are fulfilled.

## Usage

1. Clone the repository
2. Create an `absences.txt` file in the same directory, and put in departure and return dates for the trips like so:
    ```
    2023/1/15 - 2023/1/22
    2023/3/24 - 2023/3/27
    2023/6/4 - 2023/7/16
    ```
3. In the same directory, run the checker with `python checker.py`
