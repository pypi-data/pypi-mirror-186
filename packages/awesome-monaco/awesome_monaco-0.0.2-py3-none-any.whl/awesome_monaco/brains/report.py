from brains.build_data import RacerInfo
from brains.config import limit, line_length


def print_report(report: {str: RacerInfo}, reverse=True):
    """Проблемма не в двух словарях а как правильно Reverce реализовывать"""
    racers = list(report.values())

    cut_position = -limit if reverse else limit
    before_line = racers[:cut_position]
    after_line = racers[cut_position:]

    for racer in before_line:
        go_print(racer)
    print("_" * line_length)
    for racer in after_line:
        go_print(racer)


def go_print(racer: RacerInfo):
    print(f"{racer.place : <3}| {racer.name : <18}  {racer.team : <30} | {str(racer.lap_time)}" )