from demo.gossiping_bus_drivers.simulation import simulate_drive_till_equal
from demo.gossiping_bus_drivers.driver import Driver
from demo.gossiping_bus_drivers.route import Route
from demo.gossiping_bus_drivers.rumor import Rumor
from demo.gossiping_bus_drivers.stop import Stop


class TestGossip:

    def setup_method(self):
        self._stop1 = Stop("stop1")
        self._stop2 = Stop("stop2")
        self._stop3 = Stop("stop3")
        self._route1 = Route([self._stop1, self._stop2])
        self._route2 = Route([self._stop1, self._stop2, self._stop3])
        self._rumor1 = Rumor("Rumor1")
        self._rumor2 = Rumor("Rumor2")
        self._rumor3 = Rumor("Rumor3")
        self._driver1 = Driver("Driver1", self._route1, [self._rumor1])
        self._driver2 = Driver("Driver2", self._route2, [self._rumor2, self._rumor3])

    def test_driver_starts_at_first_stop_in_route(self):
        assert self._stop1 == self._driver1.get_stop()

    def test_driver_drivers_to_next_stop(self):
        self._driver1.drive()
        assert self._stop2 == self._driver1.get_stop()

    def test_driver_returns_to_start_after_last_stop(self):
        self._driver1.drive()
        self._driver1.drive()
        assert self._stop1 == self._driver1.get_stop()

    def test_first_stop_has_drivers_at_start(self):
        assert self._stop1.get_drivers() == [self._driver1, self._driver2]
        assert self._stop2.get_drivers() == []

    def test_multiple_drivers_enter_and_leave_stops(self):
        # init
        assert self._stop1.get_drivers() == [self._driver1, self._driver2]
        assert self._stop2.get_drivers() == []
        assert self._stop3.get_drivers() == []
        # first drive
        self._driver1.drive()
        self._driver2.drive()
        assert self._stop1.get_drivers() == []
        assert self._stop2.get_drivers() == [self._driver1, self._driver2]
        assert self._stop3.get_drivers() == []
        # second drive
        self._driver1.drive()
        self._driver2.drive()
        assert self._stop1.get_drivers() == [self._driver1]
        assert self._stop2.get_drivers() == []
        assert self._stop3.get_drivers() == [self._driver2]
        # third drive
        self._driver1.drive()
        self._driver2.drive()
        assert self._stop1.get_drivers() == [self._driver2]
        assert self._stop2.get_drivers() == [self._driver1]
        assert self._stop3.get_drivers() == []

    def test_drivers_have_rumors_at_start(self):
        assert self._driver1.get_rumors() == set([self._rumor1])
        assert self._driver2.get_rumors() == set([self._rumor2, self._rumor3])

    def test_no_drivers_gossip_at_empty_stop(self):
        self._stop2.gossip()
        assert self._driver1.get_rumors() == set([self._rumor1])
        assert self._driver2.get_rumors() == set([self._rumor2, self._rumor3])

    def test_drivers_gossip_at_stop(self):
        self._stop1.gossip()
        assert self._driver1.get_rumors() == set([self._rumor1, self._rumor2, self._rumor3])
        assert self._driver2.get_rumors() == set([self._rumor1, self._rumor2, self._rumor3])

    def test_gossip_is_not_duplicated(self):
        self._stop1.gossip()
        self._stop1.gossip()
        assert self._driver1.get_rumors() == set([self._rumor1, self._rumor2, self._rumor3])
        assert self._driver2.get_rumors() == set([self._rumor1, self._rumor2, self._rumor3])

    def test_drive_till_equal_test(self):
        assert 1 == simulate_drive_till_equal([self._driver1, self._driver2])


def test_acceptance1():
    s1 = Stop("s1")
    s2 = Stop("s2")
    s3 = Stop("s3")
    s4 = Stop("s4")
    s5 = Stop("s5")
    r1 = Route([s3, s1, s2, s3])
    r2 = Route([s3, s2, s3, s1])
    r3 = Route([s4, s2, s3, s4, s5])
    d1 = Driver("d1", r1, [Rumor("1")])
    d2 = Driver("d2", r2, [Rumor("2")])
    d3 = Driver("d3", r3, [Rumor("3")])
    assert 6 == simulate_drive_till_equal([d1, d2, d3])


def test_acceptance2():
    s1 = Stop("s1")
    s2 = Stop("s2")
    s5 = Stop("s5")
    s8 = Stop("s8")
    r1 = Route([s2, s1, s2])
    r2 = Route([s5, s2, s8])
    d1 = Driver("d1", r1, [Rumor("1")])
    d2 = Driver("d2", r2, [Rumor("2")])
    assert 480 == simulate_drive_till_equal([d1, d2])
