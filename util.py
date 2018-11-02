from datetime import datetime
import csv

def validate_date(date_text):

    try:
        datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def open_file():    
        filename = 'Daily Summaries.csv'
        with open(filename) as f:
            reader = csv.reader(f)
            return reader
