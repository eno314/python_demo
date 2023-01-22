from datetime import date, timedelta
from demo.nearest_and_its_prev_and_next_date.repository import DemoRepository
from demo.nearest_and_its_prev_and_next_date.usecase import Usecase


def setup_usecase_having_demo_repository_with_many_data(size):
    repository = DemoRepository()
    date_list = [date(2023, 1, 1) + timedelta(days=i) for i in range(365)]
    for _ in range(size):
        repository.add_dates(date_list)
    return Usecase(repository)


def test_performance_v1(benchmark):
    sut = setup_usecase_having_demo_repository_with_many_data(1)
    result = benchmark(
        sut.find_nearest_and_its_prev_and_next_date_v1,
        date(2023, 12, 31)
    )
    assert result


def test_performance_v2(benchmark):
    sut = setup_usecase_having_demo_repository_with_many_data(1)
    result = benchmark(
        sut.find_nearest_and_its_prev_and_next_date_v2,
        date(2023, 12, 31)
    )
    assert result


def test_performance_10times_v1(benchmark):
    sut = setup_usecase_having_demo_repository_with_many_data(10)
    result = benchmark(
        sut.find_nearest_and_its_prev_and_next_date_v1,
        date(2023, 12, 31)
    )
    assert result


def test_performance_10times_v2(benchmark):
    sut = setup_usecase_having_demo_repository_with_many_data(10)
    result = benchmark(
        sut.find_nearest_and_its_prev_and_next_date_v2,
        date(2023, 12, 31)
    )
    assert result


def test_performance_100times_v1(benchmark):
    sut = setup_usecase_having_demo_repository_with_many_data(100)
    result = benchmark(
        sut.find_nearest_and_its_prev_and_next_date_v1,
        date(2023, 12, 31)
    )
    assert result


def test_performance_100times_v2(benchmark):
    sut = setup_usecase_having_demo_repository_with_many_data(100)
    result = benchmark(
        sut.find_nearest_and_its_prev_and_next_date_v2,
        date(2023, 12, 31)
    )
    assert result


def test_performance_1000times_v1(benchmark):
    sut = setup_usecase_having_demo_repository_with_many_data(1000)
    result = benchmark(
        sut.find_nearest_and_its_prev_and_next_date_v1,
        date(2023, 12, 31)
    )
    assert result


def test_performance_1000times_v2(benchmark):
    sut = setup_usecase_having_demo_repository_with_many_data(1000)
    result = benchmark(
        sut.find_nearest_and_its_prev_and_next_date_v2,
        date(2023, 12, 31)
    )
    assert result
