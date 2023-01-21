import datetime
import pytest

from demo.latest_and_its_prev_and_next_date.repository import DemoRepository


def setup_demo_repository_having_data():
    date_list = [
        datetime.date(2023, 1, 1),
        datetime.date(2023, 1, 10),
        datetime.date(2023, 1, 20),
        datetime.date(2023, 1, 30)
    ]
    return DemoRepository(date_list)


def setup_demo_repository_having_no_data():
    return DemoRepository([])


class Test_find_latest_date:

    @pytest.mark.parametrize(('target_date', 'expected'), [
        # When target date is less than min Then return min
        (datetime.date(2022, 12, 31), datetime.date(2023, 1, 1)),
        # When target date is equal to min Then return min
        (datetime.date(2023, 1, 1), datetime.date(2023, 1, 1)),
        # When_target_date is between min and max Then return latest
        (datetime.date(2023, 1, 18), datetime.date(2023, 1, 20)),
        # When target date is equal to max Then return max
        (datetime.date(2023, 1, 30), datetime.date(2023, 1, 30)),
        # When target date is greater than max Then return max
        (datetime.date(2023, 2, 1), datetime.date(2023, 1, 30)),
    ])
    def test_given_repository_having_data(self, target_date, expected):
        sut = setup_demo_repository_having_data()
        actual = sut.find_latest_date(target_date)
        assert actual == expected

    @pytest.mark.parametrize(('target_date'), [
        (datetime.date(2022, 12, 31)),
        (datetime.date(2023, 1, 1)),
        (datetime.date(2023, 1, 18)),
        (datetime.date(2023, 1, 30)),
        (datetime.date(2023, 2, 1)),
    ])
    def test_given_repository_having_no_data_then_return_none(
        self, target_date
    ):
        sut = setup_demo_repository_having_no_data()
        actual = sut.find_latest_date(target_date)
        assert actual is None


class Test_find_prev_date:

    @pytest.mark.parametrize(('target_date', 'expected'), [
        # When target date is less than min Then return None
        (datetime.date(2022, 12, 31), None),
        # When target date is equal to min Then return min
        (datetime.date(2023, 1, 1), None),
        # When_target_date is between min and max Then return previous
        (datetime.date(2023, 1, 18), datetime.date(2023, 1, 10)),
        # When target date is equal to max Then return prev to max
        (datetime.date(2023, 1, 30), datetime.date(2023, 1, 20)),
        # When target date is greater than max Then return max
        (datetime.date(2023, 2, 1), datetime.date(2023, 1, 30)),
    ])
    def test_given_repository_having_data(self, target_date, expected):
        sut = setup_demo_repository_having_data()
        actual = sut.find_prev_date(target_date)
        assert actual == expected

    @pytest.mark.parametrize(('target_date'), [
        (datetime.date(2022, 12, 31)),
        (datetime.date(2023, 1, 1)),
        (datetime.date(2023, 1, 18)),
        (datetime.date(2023, 1, 30)),
        (datetime.date(2023, 2, 1)),
    ])
    def test_given_repository_having_no_data_then_return_none(
        self, target_date
    ):
        sut = setup_demo_repository_having_no_data()
        actual = sut.find_prev_date(target_date)
        assert actual is None


class Test_find_next_date:

    @pytest.mark.parametrize(('target_date', 'expected'), [
        # When target date is less than min Then return min
        (datetime.date(2022, 12, 31), datetime.date(2023, 1, 1)),
        # When target date is equal to min Then return next to min
        (datetime.date(2023, 1, 1), datetime.date(2023, 1, 10)),
        # When_target_date is between min and max Then return next
        (datetime.date(2023, 1, 18), datetime.date(2023, 1, 20)),
        # When target date is equal to max Then return None
        (datetime.date(2023, 1, 30), None),
        # When target date is greater than max Then return None
        (datetime.date(2023, 2, 1), None),
    ])
    def test_given_repository_having_data(self, target_date, expected):
        sut = setup_demo_repository_having_data()
        actual = sut.find_next_date(target_date)
        assert actual == expected

    @pytest.mark.parametrize(('target_date'), [
        (datetime.date(2022, 12, 31)),
        (datetime.date(2023, 1, 1)),
        (datetime.date(2023, 1, 18)),
        (datetime.date(2023, 1, 30)),
        (datetime.date(2023, 2, 1)),
    ])
    def test_given_repository_having_no_data_then_return_none(
        self, target_date
    ):
        sut = setup_demo_repository_having_no_data()
        actual = sut.find_next_date(target_date)
        assert actual is None
