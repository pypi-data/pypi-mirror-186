import datetime

date_format = "%Y-%m-%d"
datetime_format = "%Y-%m-%d %H:%M:%S"


def create_datetime(custom_date):
    date_to_search = custom_date if custom_date else datetime.date.today() - datetime.timedelta(days=1)
    return datetime.datetime.strptime(str(date_to_search), date_format).replace(tzinfo=datetime.timezone.utc)


def create_date(custom_date):
    return create_datetime(custom_date).date()


def get_str_for_date(custom_date):
    return custom_date.strftime(date_format)


def get_str_for_datetime(custom_datetime):
    return custom_datetime.strftime(datetime_format)
