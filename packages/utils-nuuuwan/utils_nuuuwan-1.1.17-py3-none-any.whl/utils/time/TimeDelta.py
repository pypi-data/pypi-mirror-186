class TimeDelta:
    def __init__(self, dut: int = 0):
        self.dut = dut

    def __eq__(self, other) -> bool:
        return self.dut == other.dut

    def humanize(self):
        dut = self.dut
        if dut < 60:
            return f'{dut:.0f}sec'
        dut /= 60
        if dut < 60:
            return f'{dut:.0f}min'
        dut /= 60
        if dut < 24:
            return f'{dut:.0f}hr'
        dut /= 24
        return f'{dut:.0f}day'
