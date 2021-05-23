import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from datetime import date


class BurnDown:
    periods = 0

    def __init__(self, periods=7):
        self.periods = periods

    def show(self):
        times = pd.date_range(date.today(), periods=self.periods, freq="D")

        fig, axes = plt.subplots(1)
        fig.autofmt_xdate()
        plt.plot(times, range(times.size))

        date_format = mdates.DateFormatter("%y-%m-%d")
        axes.xaxis.set_major_formatter(date_format)

        plt.show()


burndown = BurnDown()
burndown.show()
