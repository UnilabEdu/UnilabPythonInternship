def calculate_age(dob):
    """
    calculates age based on date of birth
    date of birth (dob) should be a Python date object (from datetime module)
    """
    from datetime import date
    today = date.today()
    return int((today - dob).days / 365.2422)


def dob_string_to_datetime(received_date):
    """
    converts received_date from a 'YYYY-MM-DD' string to a Python datetime object
    returns a date object
    """
    from datetime import date
    tuple_date = tuple((int(t)) for t in received_date.split('-'))
    return date(*tuple_date)
