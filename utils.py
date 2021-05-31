import pandas as pd
from datetime import date, timedelta


def get_time_series(start, week=1, revision=1, freq="D"):
    return pd.date_range(start, periods=week * 7 + revision, freq=freq).to_series()


def is_weekend(time):
    """
    datetime -> bool

    입력한 날짜가 토요일 또는 일요일인지를 반환
    """
    return time.dayofweek in [5, 6]


def add_time(day=date.today(), days=0):
    return day + timedelta(days)


def str_to_bool(input):
    """
    str -> bool

    입력 스트링이 bool 형태에 맞는지를 반환
    """
    return input.upper() in ["TRUE", "1"]
