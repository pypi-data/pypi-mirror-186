from datetime import datetime


class MyClass:
    def __init__(self, value):
        self._value = value

    def _get_value(self):
        return self._value

    def _set_value(self, value):
        if value < 0:
            raise ValueError("Value must be non-negative.")
        self._value += value

    value = property(_get_value, _set_value)

class RacerInfo:
    def __init__(self, place=None, name=None, team=None):
        self.place = place
        self.name = name
        self.team = team
        self.lap_time = None

    def calculate_lap_time(self, start_time, end_time):
        time_delta = start_time - end_time
        self.lap_time = time_delta

    def get_info(self,spacer):
        name_and_team = self.name + " " + self.team
        return self.place + " | " + name_and_team.ljust(spacer," ") + " | " + str(self.lap_time)
    @property
    def get_time(self):
        return self.lap_time

    def set_time(self, time):
        self.lap_time += time

date2 = datetime(2022, 1, 1, 12, 30, 0)

a = RacerInfo()
a.set_time(10)
print(a.lap_time)
a.set_time(-15)
print(a.lap_time)
a.set_time(date2)
print(a.lap_time)