import datetime


def check_date_is_in_future(date_text):
    '''Verifies if a date in the format DD/MM/YYYY is in the future'''
    date = datetime.datetime.strptime(date_text, '%d/%m/%Y')
    if date < datetime.datetime.now():
        exception = ValueError(f"Date {date_text} is in the past")
        raise exception


def check_date_is_valid(date_text):
    '''Verifies if a date in the format DD/MM/YYYY is valid'''
    try:
        datetime.datetime.strptime(date_text, '%d/%m/%Y')
    except ValueError:
        print(f"Date {date_text} is not valid")
