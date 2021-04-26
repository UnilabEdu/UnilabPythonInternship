def calculate_age(dob):
    from datetime import date
    today = date.today()
    return int((today - dob).days / 365.2422)


def dob_string_to_datetime(received_date):
    from datetime import date
    tuple_date = tuple((int(t)) for t in received_date.split('-'))
    return date(*tuple_date)
