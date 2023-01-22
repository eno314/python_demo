from datetime import date
from typing import Tuple
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
