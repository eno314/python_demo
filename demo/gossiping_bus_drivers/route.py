class Route:
    def __init__(self, stops):
        self._stops = stops

    def get(self, stop_number):
        return self._stops[stop_number]

    def get_next_stop(self, stop_number):
        return (stop_number + 1) % len(self._stops)

    def stop_at(self, driver, stop_number):
        self._stops[stop_number].add_driver(driver)

    def leave(self, driver, stop_number):
        self._stops[stop_number].remove_driver(driver)
