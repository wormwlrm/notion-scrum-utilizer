import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import timedelta
import utils
from src.Config import Config


class BurnChart(Config):
    def __init__(self):
        super().__init__()

    def get_ideal_series(self, times, task):
        series = []
        weekday = 5

        task_per_day = float(task / (weekday * self.SPRINT_WEEK))
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

    def create_image(
        self,
        data,
        task_count=0,
        x_label="Time Series",
        y_label="Task Count",
    ):
        task_count = task_count
        times = utils.get_time_series(
            start=utils.add_time(days=self.SPRINT_WEEK * -7), week=self.SPRINT_WEEK
        )

        fig, axes = plt.subplots(1)
        fig.autofmt_xdate()

        plt.grid(True, axis="x", linestyle="--")

        plt.plot(
            times,
            self.get_ideal_series(times=times, task=task_count),
            color="red",
            alpha=0.7,
            label="Ideal Chart",
        )

        plt.plot(
            times,
            data,
            color="grey",
            marker=".",
            alpha=0.3,
        )
        plt.plot(
            times,
            data,
            drawstyle="steps",
            color="blue",
            alpha=0.7,
            label="Actual Chart",
        )

        plt.legend()

        # 주말 영역은 색칠하기
        for time in times[:-1]:
            if utils.is_weekend(time):
                plt.axvspan(
                    time,
                    time + timedelta(days=1),
                    facecolor="0.2",
                    alpha=0.1,
                )

        plt.xlabel(x_label)
        plt.ylabel(y_label)

        date_format = mdates.DateFormatter("%m-%d")
        axes.xaxis.set_major_formatter(date_format)

        plt.savefig("burnchart.png")
