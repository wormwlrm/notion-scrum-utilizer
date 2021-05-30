import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from datetime import date, timedelta

# from main import scrum


class BurnChart:
    periods = 0
    task_count = 0
    x_label = "Time Series"
    y_label = "Task Count"

    def __init__(
        self, periods=7, x_label="Time Series", y_label="Task Count", task_count=0
    ):
        self.periods = periods
        self.x_label = x_label
        self.y_label = y_label
        self.task_count = task_count

    def get_time_series(self, day=date.today(), revision=1):
        return pd.date_range(day, periods=self.periods + revision, freq="D").to_series()

    def is_weekend(self, time):
        return time.dayofweek in [5, 6]

    def add_time(self, day=date.today(), days=0):
        return day + timedelta(days)

    def get_ideal_series(self, times, task):
        series = []

        task_per_day = float(task / (self.periods - 2))
        remain_task = task

        for (index, time) in enumerate(times):
            if index == 0:
                series.append(remain_task)
                continue

            time = self.add_time(time, -1)

            if self.is_weekend(time):
                series.append(remain_task)
            else:
                remain_task -= task_per_day
                series.append(remain_task)

        return series

    def show(self):
        task_count = self.task_count
        times = self.get_time_series(self.add_time(days=0))

        fig, axes = plt.subplots(1)
        fig.autofmt_xdate()

        plt.grid(True, axis="x", linestyle="--")
        plt.plot(times, self.get_ideal_series(times=times, task=task_count))

        # 주말 영역은 색칠하기
        for time in times[:-1]:
            if self.is_weekend(time):
                plt.axvspan(
                    time,
                    time + timedelta(days=1),
                    facecolor="0.2",
                    alpha=0.1,
                )

        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)

        date_format = mdates.DateFormatter("%m-%d")
        axes.xaxis.set_major_formatter(date_format)

        plt.show()
