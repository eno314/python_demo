def simulate_drive_till_equal(drivers):
    time = 0
    while _not_all_rumors(drivers) and time < 480:
        _drive_and_gossip(drivers)
        time += 1
    return time


def _drive_and_gossip(drivers):
    stops = set([])
    for driver in drivers:
        driver.drive()
        stops.add(driver.get_stop())
    for stop in stops:
        stop.gossip()


def _not_all_rumors(drivers):
    rumors = set([])
    for driver in drivers:
        rumors.update(driver.get_rumors())
    for driver in drivers:
        if driver.get_rumors() != rumors:
            return True
    return False
