class Driver:

    def __init__(self, name, route, rumors):
        self._name = name
        self._route = route
        self._rumors = set(rumors)
        self._stop_number = 0
        self._route.stop_at(self, self._stop_number)

    def get_stop(self):
        return self._route.get(self._stop_number)

    def drive(self):
        self._route.leave(self, self._stop_number)
        self._stop_number = self._route.get_next_stop(self._stop_number)
        self._route.stop_at(self, self._stop_number)

    def get_rumors(self):
        return self._rumors

    def add_rumors(self, rumors):
        self._rumors.update(rumors)
