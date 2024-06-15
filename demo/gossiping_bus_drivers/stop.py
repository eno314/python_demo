class Stop:
    def __init__(self, name):
        self._name = name
        self._drivers = []

    def get_drivers(self):
        return self._drivers

    def add_driver(self, driver):
        self._drivers.append(driver)

    def remove_driver(self, driver):
        if driver in self._drivers:
            self._drivers.remove(driver)

    def gossip(self):
        rumors_at_atop = set([])
        for driver in self._drivers:
            rumors_at_atop.update(driver.get_rumors())
        for driver in self._drivers:
            driver.add_rumors(rumors_at_atop)
