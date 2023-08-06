import time

from utils.time.TimeDelta import TimeDelta


class Time:
    def __init__(self, ut: int = None):
        if ut is None:
            ut = time.time()
        self.ut = ut

    def __eq__(self, other) -> bool:
        return self.ut == other.ut

    def __sub__(self, other) -> TimeDelta:
        return TimeDelta(self.ut - other.ut)

    def __add__(self, other: TimeDelta):
        return Time(self.ut + other.dut)

    @staticmethod
    def now():
        return Time()
