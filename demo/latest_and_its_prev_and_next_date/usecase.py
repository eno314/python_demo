from datetime import date
from typing import List, Tuple
from demo.latest_and_its_prev_and_next_date.repository import Repository


class Usecase:
    def __init__(self, repository: Repository):
        self.repository = repository

    def find_latest_and_its_prev_and_next_date_v1(
        self, target: date
    ) -> Tuple[date, date, date]:
        latest_date = self.repository.find_latest_date(target)
        if latest_date is None:
            return None, None, None
        prev_date = self.repository.find_prev_date(latest_date)
        next_date = self.repository.find_next_date(latest_date)
        return latest_date, prev_date, next_date

    def find_latest_and_its_prev_and_next_date_v2(
        self, target: date
    ) -> Tuple[date, date, date]:
        all_dates = self.repository.find_all_date_list()
        latest_index = self._find_latest_index_from_dates(all_dates, target)
        return (
            self._get_date_or_none_from_dates(all_dates, latest_index),
            self._get_date_or_none_from_dates(all_dates, latest_index - 1),
            self._get_date_or_none_from_dates(all_dates, latest_index + 1),
        )

    def _find_latest_index_from_dates(
        self, dates: List[date], target: date
    ) -> int:
        latest_index = 0
        for index in range(1, len(dates)):
            date_diff_days = abs((dates[index] - target).days)
            latest_diff_days = abs((dates[latest_index] - target).days)
            if date_diff_days < latest_diff_days:
                latest_index = index
            else:
                break
        return latest_index

    def _get_date_or_none_from_dates(
        self, dates: List[date], index: int
    ) -> date:
        return dates[index] if 0 <= index < len(dates) else None
