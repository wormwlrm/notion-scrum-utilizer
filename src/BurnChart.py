import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import timedelta
import utils


class BurnChart:
    periods = 0
    task_count = 0
    x_label = "Time Series"
    y_label = "Task Count"
    data = []

    def __init__(
        self, data, periods=7, x_label="Time Series", y_label="Task Count", task_count=0
    ):
        self.data = data
        self.periods = periods
        self.x_label = x_label
        self.y_label = y_label
        self.task_count = task_count

    def get_ideal_series(self, times, task):
        series = []

        task_per_day = float(task / (self.periods - 2))
        remain_task = task

        for (index, time) in enumerate(times):
            if index == 0:
                series.append(remain_task)
                continue

            time = utils.add_time(time, -1)

            if utils.is_weekend(time):
                series.append(remain_task)
            else:
                remain_task -= task_per_day
                series.append(remain_task)

        return series

    def show(self):
        task_count = self.task_count
        times = utils.get_time_series(utils.add_time(days=-7))

        fig, axes = plt.subplots(1)
        fig.autofmt_xdate()

        plt.grid(True, axis="x", linestyle="--")
        plt.plot(
            times, self.get_ideal_series(times=times, task=task_count), color="red"
        )
        plt.plot(times, self.data, color="blue")

        # 주말 영역은 색칠하기
        for time in times[:-1]:
            if utils.is_weekend(time):
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
