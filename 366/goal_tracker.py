import calendar
from datetime import date
from typing import Tuple

"""
Sample text if on-track:
Congratulations! You are on track with your steps goal. The target for 2023-01-12 is 164,383 steps and you are 11 ahead.

Sample text if not on track:
You have some catching up to do! The target for 2023-09-30 is 27,300 pages read and you are 2 behind.
"""


def goal_tracker(desc: str, annual_target: int, current_score: int, score_date: Tuple[int, int, int]):
     """Return a string determining whether a goal is on track
     by calculating the current target and comparing it with the current achievement.
     The function assumes the goal is to be achieved in a calendar year. Think New Year's Resolution :)
     """
     pass