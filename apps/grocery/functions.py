import datetime


def get_seven_days_from_now():
    return (datetime.datetime.now() + datetime.timedelta(days=7))
