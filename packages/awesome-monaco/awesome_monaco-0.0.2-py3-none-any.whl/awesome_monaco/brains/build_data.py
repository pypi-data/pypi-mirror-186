import datetime
from os import path
from brains.config import RACERS, START, END, racers_type
from brains.utils import calculate_critical_threshold
from datetime import datetime


class RacerInfo:
    def __init__(self, place=None, name=None, team=None):
        self.place = place
        self.name = name
        self.team = team
        self.lap_time = False

    @property
    def set_time(self):
        return self.lap_time

    @set_time.setter
    def set_time(self, time):
        if self.lap_time:
            self.lap_time = time - self.lap_time
        else:
            self.lap_time = time


def find_driver(driver, data):
    drivers_dict = {value.name: key for key, value in data.items()}
    abr_driver = drivers_dict[driver]
    return abr_driver


def reverse_data(data):
    initials = list(data.keys())
    initials.reverse()
    new_data = {abr: data[abr] for abr in initials}
    return new_data


def build_report(folder, driver: str = None, reverse: bool = False):
    data = collect_data(folder)
    data, mistakes = add_rating_to_data(data)
    data = {**data, **mistakes}
    if reverse:
        data = reverse_data(data)
    if driver:
        abr_driver = find_driver(driver, data)
        data = {abr_driver: data[abr_driver]}
    return data


def collect_data(folder):
    abbreviations = read_file(folder, RACERS)
    abbreviations = [abr.split("_") for abr in abbreviations]
    data_collection = {initial: RacerInfo(name=name, team=team) for initial, name, team in abbreviations}
    start_time, end_time = read_file(folder, START), read_file(folder, END)
    data_collection = add_time(start_time, end_time, data_collection)
    return data_collection


def add_rating_to_data(data_collection: {str: RacerInfo}):
    data = sort_data(data_collection)
    mistakes = {}
    counter = 1
    for abr, racer in data.items():
        if racer.lap_time.total_seconds() <= calculate_critical_threshold(racers_type):
            racer.lap_time = "INVALID TIME"
            racer.place = "DNF"
            mistakes[abr] = racer
        else:
            racer.place = counter
            counter += 1
    for abr in mistakes.keys():
        data.pop(abr)
    return data, mistakes


def read_file(folder, file):
    with open(path.join(folder, file), "r", encoding='utf-8') as record:
        text = record.read().strip().split("\n")
    return text


def add_time(start_time_list: list, end_time_list: list, data: {str: RacerInfo}) -> {str: RacerInfo}:
    start_time = [parce_time(line) for line in start_time_list]
    end_time = [parce_time(line) for line in end_time_list]
    together = start_time + end_time

    for abr, time in together:
        racer = data.get(abr)
        racer.set_time = time
        data[abr] = racer
    return data


def parce_time(line):
    line = line.strip()
    initials = line[:3]
    time_string = line[3:]
    time = datetime.strptime(time_string, '%Y-%m-%d_%H:%M:%S.%f')
    return initials, time


def sort_data(data):
    abr = list(data.keys())
    lap_time = [time.lap_time for time in data.values()]
    abr_lap_time = dict(zip(lap_time, abr))
    lap_time.sort()
    racers = {}
    for lap in lap_time:
        abr = abr_lap_time[lap]
        racers[abr] = data[abr]
    return racers
