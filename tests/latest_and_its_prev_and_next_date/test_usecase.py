
from datetime import date, timedelta
import pytest

from demo.latest_and_its_prev_and_next_date.repository import DemoRepository
from demo.latest_and_its_prev_and_next_date.usecase import Usecase


def setup_usecase_having_demo_repository_with_simple_date():
    repository = DemoRepository()
    repository.add_dates([
        date(2023, 1, 1),
        date(2023, 1, 10),
        date(2023, 1, 20),
        date(2023, 1, 30)
    ])
    return Usecase(repository)


def setup_usecase_having_demo_repository_with_no_date():
    return Usecase(DemoRepository())


class Test_find_latest_and_its_prev_and_next_date_v1:

    @pytest.mark.parametrize(('target', 'expected'), [
        # When target date is less than min Then return (min, None, next to min)
        (
            date(2022, 12, 31),
            (date(2023, 1, 1), None, date(2023, 1, 10)),
        ),
        # When target date is equal to min Then return (min, None, next to min)
        (
            date(2023, 1, 1),
            (date(2023, 1, 1), None, date(2023, 1, 10)),
        ),
        # When_target_date is between min and max Then return (latest, prev to latest, next to latest)
        (
            date(2023, 1, 18),
            (date(2023, 1, 20), date(2023, 1, 10), date(2023, 1, 30)),
        ),
        # When target date is equal to max Then return (max, prev to max, None)
        (
            date(2023, 1, 30),
            (date(2023, 1, 30), date(2023, 1, 20), None),
        ),
        # When target date is greater than max Then return (max, prev to max, None)
        (
            date(2023, 2, 1),
            (date(2023, 1, 30), date(2023, 1, 20), None),
        ),
    ])
    def test_find_latest_and_its_prev_and_next_date_v1_having_data(
        self, target, expected
    ):
        sut = setup_usecase_having_demo_repository_with_simple_date()
        actual = sut.find_latest_and_its_prev_and_next_date_v1(target)
        assert actual == expected

    @pytest.mark.parametrize(('target_date'), [
        (date(2022, 12, 31)),
        (date(2023, 1, 1)),
        (date(2023, 1, 18)),
        (date(2023, 1, 30)),
        (date(2023, 2, 1)),
    ])
    def test_find_latest_and_its_prev_and_next_date_v1_having_no_data(
        self, target_date
    ):
        sut = setup_usecase_having_demo_repository_with_no_date()
        actual = sut.find_latest_and_its_prev_and_next_date_v1(target_date)
        assert actual == (None, None, None)


class Test_find_latest_and_its_prev_and_next_date_v2:

    @pytest.mark.parametrize(('target', 'expected'), [
        # When target date is less than min Then return (min, None, next to min)
        (
            date(2022, 12, 31),
            (date(2023, 1, 1), None, date(2023, 1, 10)),
        ),
        # When target date is equal to min Then return (min, None, next to min)
        (
            date(2023, 1, 1),
            (date(2023, 1, 1), None, date(2023, 1, 10)),
        ),
        # When_target_date is between min and max Then return (latest, prev to latest, next to latest)
        (
            date(2023, 1, 18),
            (date(2023, 1, 20), date(2023, 1, 10), date(2023, 1, 30)),
        ),
        # When target date is equal to max Then return (max, prev to max, None)
        (
            date(2023, 1, 30),
            (date(2023, 1, 30), date(2023, 1, 20), None),
        ),
        # When target date is greater than max Then return (max, prev to max, None)
        (
            date(2023, 2, 1),
            (date(2023, 1, 30), date(2023, 1, 20), None),
        ),
    ])
    def test_find_latest_and_its_prev_and_next_date_v2_having_data(
        self, target, expected
    ):
        sut = setup_usecase_having_demo_repository_with_simple_date()
        actual = sut.find_latest_and_its_prev_and_next_date_v2(target)
        assert actual == expected

    @pytest.mark.parametrize(('target_date'), [
        (date(2022, 12, 31)),
        (date(2023, 1, 1)),
        (date(2023, 1, 18)),
        (date(2023, 1, 30)),
        (date(2023, 2, 1)),
    ])
    def test_find_latest_and_its_prev_and_next_date_v2_having_no_data(
        self, target_date
    ):
        sut = setup_usecase_having_demo_repository_with_no_date()
        actual = sut.find_latest_and_its_prev_and_next_date_v2(target_date)
        assert actual == (None, None, None)


class Test_performance:

    def test_performance_v1(self, benchmark):
        sut = self._setup_usecase_having_demo_repository_with_many_data(1)
        result = benchmark(
            sut.find_latest_and_its_prev_and_next_date_v1,
            date(2023, 12, 31)
        )
        assert result

    def test_performance_v2(self, benchmark):
        sut = self._setup_usecase_having_demo_repository_with_many_data(1)
        result = benchmark(
            sut.find_latest_and_its_prev_and_next_date_v2,
            date(2023, 12, 31)
        )
        assert result

    def test_performance_10times_v1(self, benchmark):
        sut = self._setup_usecase_having_demo_repository_with_many_data(10)
        result = benchmark(
            sut.find_latest_and_its_prev_and_next_date_v1,
            date(2023, 12, 31)
        )
        assert result

    def test_performance_10times_v2(self, benchmark):
        sut = self._setup_usecase_having_demo_repository_with_many_data(10)
        result = benchmark(
            sut.find_latest_and_its_prev_and_next_date_v2,
            date(2023, 12, 31)
        )
        assert result

    def test_performance_100times_v1(self, benchmark):
        sut = self._setup_usecase_having_demo_repository_with_many_data(100)
        result = benchmark(
            sut.find_latest_and_its_prev_and_next_date_v1,
            date(2023, 12, 31)
        )
        assert result

    def test_performance_100times_v2(self, benchmark):
        sut = self._setup_usecase_having_demo_repository_with_many_data(100)
        result = benchmark(
            sut.find_latest_and_its_prev_and_next_date_v2,
            date(2023, 12, 31)
        )
        assert result

    def test_performance_1000times_v1(self, benchmark):
        sut = self._setup_usecase_having_demo_repository_with_many_data(1000)
        result = benchmark(
            sut.find_latest_and_its_prev_and_next_date_v1,
            date(2023, 12, 31)
        )
        assert result

    def test_performance_1000times_v2(self, benchmark):
        sut = self._setup_usecase_having_demo_repository_with_many_data(1000)
        result = benchmark(
            sut.find_latest_and_its_prev_and_next_date_v2,
            date(2023, 12, 31)
        )
        assert result

    def _setup_usecase_having_demo_repository_with_many_data(self, size):
        repository = DemoRepository()
        date_list = [date(2023, 1, 1) + timedelta(days=i) for i in range(365)]
        for _ in range(size):
            repository.add_dates(date_list)
        return Usecase(repository)
