from __future__ import annotations
import datetime


StatsType = "dict[str, dict[str, dict[str, dict[str, list[int]]]]]"


def get_last_month_date(date: datetime.date) -> datetime.date:
    year, month = date.year, date.month
    if month == 1:
        year -= 1
        month = 12
    else:
        month -= 1
    return date.replace(year=year, month=month)


def get_scores(stats: StatsType, last_month: datetime.date) -> tuple[float, float, int]:
    previous_scores, last_month_scores = list(), list()
    last_training = 0
    for stat in stats.values():
        for card in stat.values():
            for result in card.values():
                if result is None:
                    continue
                for date, scores in result.items():
                    date = datetime.date.fromisoformat(date)
                    if date >= last_month:
                        last_month_scores.extend(scores)
                        last_training += len(scores)
                    else:
                        previous_scores.extend(scores)
    if not previous_scores:
        previous_scores = [0]
    if not last_month_scores:
        last_month_scores = [0]
    previous_score = sum(previous_scores) / len(previous_scores)
    last_month_score = sum(last_month_scores) / len(last_month_scores)
    return previous_score, last_month_score, last_training
