from datetime import date

__version__ = "0.1"

from typing import List

# http://www.consultant.ru/law/ref/calendar/proizvodstvennye/2020b/
MOVED_HOLIDAYS: List[date] = [
    date(2020, 2, 24),
    date(2020, 3, 9),
    date(2020, 5, 4),
    date(2020, 5, 5),
    date(2020, 5, 11),
    date(2021, 2, 22),
    date(2021, 5, 3),
    date(2021, 5, 10),
    date(2021, 6, 14),
    date(2021, 11, 5),
    date(2021, 12, 31),
    date(2022, 3, 7),
    date(2022, 5, 2),
    date(2022, 5, 3),
    date(2022, 5, 10),
    date(2022, 6, 13),
    date(2023, 2, 24),
    date(2023, 5, 8),
]

WORK_WEEKENDS: List[date] = [
    date(2021, 2, 20),
    date(2022, 3, 5),
]

WEEKENDS: str = "Выходной"
MOVED_HOLIDAY: str = "Передвинутый выходной"


def is_holiday(d: date) -> str:
    # New Year's Day
    if d.month == 1 and d.day in (1, 2, 3, 4, 5, 6, 8):
        return "Новогодние каникулы"
    if d.month == 1 and d.day == 7:
        return "Рождество Христово"
    # Man Day
    if d.month == 2 and d.day == 23:
        return "День защитника Отечества"
    # Women's Day
    if d.month == 3 and d.day == 8:
        return "Международный женский день"
    # Labour Day
    if d.month == 5 and d.day == 1:
        return "Праздник Весны и Труда"
    # Victory Day
    if d.month == 5 and d.day == 9:
        return "День Победы"
    # Russia's Day
    if d.month == 6 and d.day == 12:
        return "День России"
    if d.year >= 2005:
        # Unity Day
        if d.month == 11 and d.day == 4:
            return "День народного единства"
    else:
        # October Revolution Day
        if d.month == 11 and d.day == 7:
            return "День Октябрьской революции"
    if d in MOVED_HOLIDAYS:
        return MOVED_HOLIDAY
    if d in WORK_WEEKENDS:
        return ""
    if d.weekday() in (5, 6):
        return WEEKENDS
    return ""


def check_holiday(d: date, with_weekends: bool = True) -> bool:
    r = is_holiday(d)
    if not with_weekends and r == WEEKENDS:
        return False
    return bool(r)
