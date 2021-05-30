import pandas as pd
from datetime import date, timedelta


def get_time_series(start, week=1, revision=1, freq="D"):
    return pd.date_range(start, periods=week * 7 + revision, freq=freq).to_series()


def is_weekend(time):
    return time.dayofweek in [5, 6]


def add_time(day=date.today(), days=0):
    return day + timedelta(days)
