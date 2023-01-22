from datetime import date
from typing import List, Tuple
from demo.nearest_and_its_prev_and_next_date.repository import Repository


class Usecase:
    def __init__(self, repository: Repository):
        self.repository = repository

    def find_nearest_and_its_prev_and_next_date_v1(
        self, target: date
    ) -> Tuple[date, date, date]:
        nearest_date = self.repository.find_nearest_date(target)
        if nearest_date is None:
            return None, None, None
        prev_date = self.repository.find_prev_date(nearest_date)
        next_date = self.repository.find_next_date(nearest_date)
        return nearest_date, prev_date, next_date

    def find_nearest_and_its_prev_and_next_date_v2(
        self, target: date
    ) -> Tuple[date, date, date]:
        all_dates = self.repository.find_sorted_all_dates()
        nearest_index = self._find_nearest_index_from_dates(all_dates, target)
        return (
            self._get_date_or_none_from_dates(all_dates, nearest_index),
            self._get_date_or_none_from_dates(all_dates, nearest_index - 1),
            self._get_date_or_none_from_dates(all_dates, nearest_index + 1),
        )

    def _find_nearest_index_from_dates(
        self, sorted_dates: List[date], target: date
    ) -> int:
        nearest_index = 0
        for index in range(1, len(sorted_dates)):
            date_diff_days = abs((sorted_dates[index] - target).days)
            nearest_diff_days = abs(
                (sorted_dates[nearest_index] - target).days)
            if date_diff_days < nearest_diff_days:
                nearest_index = index
            else:
                break
        return nearest_index

    def _get_date_or_none_from_dates(
        self, dates: List[date], index: int
    ) -> date:
        return dates[index] if 0 <= index < len(dates) else None
